import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}
'''
https://www.52shukuwang.com/xiandaidushi/8184_1.html
https://www.52shukuwang.com/xiandaidushi/8184_2.html
'''
book_title = []
chapter_url_list = []


def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'https://www.52shuku.vip/xiandaidushi/hzMX.html'

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = 'utf-8'

    # print(response_1.text)

    book_title_regex = '<h1 class="article-title">(.*)</h1>'
    # book_title_regex = '《(.*)》'
    book_title = re.findall(book_title_regex, response_1.text)

    chapter_regx = '<li class="mulu"><a href="(.*?)">第'
    chapter_url_list = re.findall(chapter_regx, response_1.text)

    # pprint(chapter_url_list)
    print(book_title)


content = ""


def getContent(url):
    global content
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = 'utf-8'

    # print(response_2.text)

    article_regx = '<article class="article-content"((\n|.)*)<div class="pagination2">'
    article = re.findall(article_regx, response_2.text)

    # pprint(article)

    content = str(article[0]).replace("\\u200c", "").replace("<br />\\n", "\n\n").replace("\\n<p>", "").replace(
        '\\u3000\\u3000', '\n').replace("</p>", "\n").strip("(<p></p>, ')\n', '\<p>\\n', '\\").strip(
        'id="nr1">').replace('&bull;', '•').replace('&nbsp;', '').replace('&hellip;', '…').replace('</p>',
                                                                                                   '\n').replace(
        '&lsquo;', "'").replace('&rsquo;', "'").replace("&ldquo;", "“").replace("&rdquo;", "”").replace("&mdash;",
                                                                                                        "—").replace(
        '\u3000', ' ')

    pprint(content)


def export():
    save_path = book_title[0].replace('/', '-') + '.txt'
    count = 0

    with open(save_path, 'a+', encoding="utf-8") as f:
        for x in chapter_url_list[0:]:
            getContent(x)

            f.write(content + '\n')

            count += 1
            print('第{}章爬取完毕！'.format(count))


getChapters()
export()
