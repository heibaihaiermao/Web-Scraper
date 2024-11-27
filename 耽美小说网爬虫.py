import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

# 小说地址，包含章节目录的信息
book_url = 'https://www.dmxs.org/cycs/13338.html'
base_url = 'https://www.dmxs.org'

'''
    https://www.dmxs.org/view/6-13338-1.html
    https://m.yushubo.net/read_118163_2.html
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}

# response_1 是通过 requests 库 get 方法向小说网址发出请求之后得到的响应，而 response_1.text 表示纯文本
session = requests.Session()
response_1 = session.get(book_url, headers=headers)

# 下面一步骤是设置编码格式，因为小说采用 utf-8 编码，一般遇到乱码可以用下面一句代码来解决
response_1.encoding = 'gb2312'
# 小说章节目录相关信息所在的文本

book_title_regex = '<h1>(.*)</h1>'
book_title = re.findall(book_title_regex, response_1.text)

chapter_regx = '<li><a href="(.*?)"> 第'
chapter_url_list = re.findall(chapter_regx, response_1.text)
new = []
for c in chapter_url_list:
    c = base_url + c
    new.append(c)
chapter_url_list = new

article_regx= '章 </p><p>(.*)</p><p></p>'

save_path = book_title[0] + '.txt'

# 定义一个变量来计数已经爬取的小说的数目
count = 0
##如果爬取的时候出现permission deny，请修改上面的sava_path,例如可以直接修改为 save_path="三寸人间.txt"
# 这样以后爬取的小说会与Python文件保存在同一个路径
# with open 语句的作用是在 C 盘创建一个叫做三寸人间.txt 的文件，'a+'表示文件以追加的形式写入，

with open(save_path, 'a+', encoding="utf-8") as f:
    for x in chapter_url_list[0:9]:
        session = requests.Session()
        response_2 = session.get(x, headers=headers)
        response_2.encoding = 'gb2312'

        article = re.findall(article_regx, response_2.text)
        content = article[0].replace('</p><p>', '\n\n')

        # 写入小说标题
        f.write('\n--------第' + str(count+1) + '章--------' + '\n\n')

        # 将小说内容这个列表中的所有元素写入文件，每写入一个就换一次行
        f.write(content)

        count += 1
        print('第{}章爬取完毕！'.format(count))
    for x in chapter_url_list[9::]:
        session = requests.Session()
        response_2 = session.get(x, headers=headers)
        response_2.encoding = 'gb2312'

        article_regx = '<p>(.*)</p>'

        article = re.findall(article_regx, response_2.text)
        content = article[0].replace('</p><p>', '\n\n')

        # 写入小说标题
        f.write('\n--------第' + str(count+1) + '章--------' + '\n\n')

        # 将小说内容这个列表中的所有元素写入文件，每写入一个就换一次行
        f.write(content)

        count += 1
        print('第{}章爬取完毕！'.format(count))