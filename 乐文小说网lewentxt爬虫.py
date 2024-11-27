import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}
'''
http://www.lw7.cc/xiaoshuo/RTcIkpMr3kE/fAfHSVCT6T4.html
https://www.52shukuwang.com/xiandaidushi/8184_2.html
'''
book_title = []
chapter_url_list = []


def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'https://www.lewentxt.org/65/65320/'
    base_url = 'https://www.lewentxt.org'

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = 'UTF-8'

    # print(response_1.text)

    book_title_regex = '《(.*)》'
    book_title = re.findall(book_title_regex, response_1.text)[0]

    chapter_regx = '<dt>《超时空男团》正文卷</dt>\n|.<dd><a href ="(.*?)">'
    chapter_url_list = re.findall(chapter_regx, response_1.text)
    chapter_url_list = chapter_url_list[6::]

    new = []
    for c in chapter_url_list:
        c = base_url + c
        new.append(c)
    chapter_url_list = new

    # pprint(chapter_url_list)
    # print(book_title)


content = ""


def getContent(url):
    global content
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = 'UTF-8'

    print(response_2.text)

    article_regx = "<div><p style='text-indent:2em; padding:0px; margin:0px;'>&nbsp;&nbsp;&nbsp;&nbsp;(.*)<br /><br /></p></div>"
    article = re.findall(article_regx, response_2.text)
    content = article[0].replace('</p><p>', '\n\n')

    pprint(content)


def export():
    save_path = book_title[0] + '.txt'
    count = 1

    with open(save_path, 'a+', encoding="UTF-8") as f:
        for x in chapter_url_list:
            getContent(x)

            f.write('\n' + "第" + str(count) +'章' + '\n')
            f.write(content + '\n')

            count += 1
            print('第{}章爬取完毕！'.format(count))

getContent('http://m.quanbl1.com/novel/57464/4619388.html')