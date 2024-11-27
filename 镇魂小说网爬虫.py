import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库

# 小说地址，包含章节目录的信息
book_url = 'https://www.zhenhunxiaoshuo.com/woxingrangwolaidianjing/'

'''
    第一章小说地址:https://www.zhenhunxiaoshuo.com/74862.html
    第二章小说地址:https://www.zhenhunxiaoshuo.com/74863.html
'''

# response_1 是通过 requests 库 get 方法向小说网址发出请求之后得到的响应，而 response_1.text 表示纯文本
response_1 = requests.get(book_url)

# 下面一步骤是设置编码格式，因为小说采用 utf-8 编码，一般遇到乱码可以用下面一句代码来解决
response_1.encoding = 'utf-8'
# 小说章节目录相关信息所在的文本
chapter = response_1.text

book_title_regex = '<h1 class="focusbox-title">(.*)</h1>'
book_title = re.findall(book_title_regex,response_1.text)

# 下面的一段注释是 response_1.text 的部分内容
'''
<article class="excerpt excerpt-c3"><a title="第1章 死循环（1）" href="https://www.zhenhunxiaoshuo.com/74862.html">第1章 死循环（1）</a></article>
     
<article class="excerpt excerpt-c3"><a title="第2章 死循环（2）" href="https://www.zhenhunxiaoshuo.com/74863.html">第2章 死循环（2）</a></article>
     
<article class="excerpt excerpt-c3"><a title="第3章 死循环（3" href="https://www.zhenhunxiaoshuo.com/74864.html">第3章 死循环（3</a></article>
  
'''

chapter_regx = '<article class="excerpt excerpt-c3"><a title=".*" href="(.*)"'
chapter_url_list = re.findall(chapter_regx, response_1.text)

print(chapter_url_list)

"""
<article class="article-content"><p>刺眼的太阳光从窗帘的缝隙透出来，天亮很久了。</p>
<p>林浔看了看时间，上午九点。</p>
<p>敲了整整一夜代码，是该去睡觉的时候了。</p>
<p>林浔：“？”</p>
</article>
"""

article_regx = '<article class="article-content">((.|\n)*)</article>'
title_regx = '<h1 class="article-title">(.*)</h1>'
content_regx = '<p>(.*?)</p>'


save_path = book_title[0]+".txt"
count = 0

with open(save_path, 'a+', encoding="utf-8") as f:
    # 从存放小说章节地址的列表中依次去除小说地址，让requests通过get方法去取货
    for x in chapter_url_list:
        # 向小说章节所在地址发送请求并获得响应

        response_2 = requests.get(x)
        response_2.encoding = 'utf-8'

        # 小说标题,匹配到的是列表

        article = re.findall(article_regx, response_2.text)
        title = re.findall(title_regx, response_2.text)
        content = str(article[0]).replace("<p>", "").replace("</p>", "").strip("()").split("\\n")

        # 写入小说标题
        f.write("\n" + title[0] + '\n')

        # 将小说内容这个列表中的所有元素写入文件，每写入一个就换一次行
        for e in content:
            f.write(e + '\n'+'\n')
        # 每成功写入一章 count 就加 1
        count += 1
        # format函数用于格式化输出
        print('第{}章爬取完毕！'.format(count))

