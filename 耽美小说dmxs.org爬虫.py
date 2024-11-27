import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}

book_title = []
chapter_url_list = []
code = "gbk"


def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'https://www.dmxs.org/cycs/12934.html'
    base_url = 'https://www.dmxs.org/view/6-12934-'
    pageTotal = 78
    pageCount = 0

    while pageCount != pageTotal:
        pageCount += 1
        chapter_url_list.append(base_url + str(pageCount) + ".html")

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = code

    # print(response_1.text)

    book_title_regex = '<title>(.*)_作者'
    book_title = re.findall(book_title_regex, response_1.text)

    # pprint(chapter_url_list)
    # print(book_title)


content = ""


def getContent(url):
    global content
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = code

    # print(response_2.text)

    article_regx = '<p>(.*)</p><p></p>'
    article = re.findall(article_regx, response_2.text)
    content = article[0].replace('</p><p>', '\n\n').replace("�", " ").replace("\u3000", " ")

    pprint(content)


def export():
    save_path = book_title[0] + '.txt'
    count = 0

    with open(save_path, 'a+', encoding=code) as f:
        for x in chapter_url_list:
            getContent(x)

            f.write(content + '\n')

            count += 1
            print('第{}章爬取完毕！'.format(count))


getChapters()
export()
