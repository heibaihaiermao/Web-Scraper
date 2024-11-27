import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

# 小说地址，包含章节目录的信息
book_url = 'https://www.256wenku.com/read/99918/'

'''
https://www.256wenku.com/read/94276/1.html
https://www.256wenku.com/read/94276/2.html
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}

session = requests.Session()
response_1 = session.get(book_url, headers=headers)
response_1.encoding = 'utf-8'


book_title_regex = 'title="(.*)">开始阅读</a></span>'
book_title = re.findall(book_title_regex, response_1.text)

chapter_regx = '<li><a href="(.*?)">第'
chapter_url_list = re.findall(chapter_regx, response_1.text)


save_path = book_title[0] + '.txt'

count = 0

with open(save_path, 'a+', encoding="utf-8") as f:
    for x in chapter_url_list:
        session = requests.Session()
        response_2 = session.get(x, headers=headers)
        response_2.encoding = 'utf-8'

        article_regx = '</p><p>(.*)<div class="page">'
        article = re.findall(article_regx, response_2.text)
        content = article[0].replace('</p><p>', '\n\n').replace("&rdquo;",'"').replace("&ldquo;",'"').replace("&hellip;","...")

        # 将小说内容这个列表中的所有元素写入文件，每写入一个就换一次行
        f.write(content+'\n')

        count += 1
        print('第{}章爬取完毕！'.format(count))
