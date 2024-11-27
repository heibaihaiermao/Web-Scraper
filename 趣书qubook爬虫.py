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
code = "GB2312"


def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'https://sj.qubook.cc/read.php?id=140236&txt=/TXT/%C8%AB%C7%F2%D7%B7%B8%FC[%BF%EC%B4%A9].txt&yeshu=0'
    base_url = book_url[0:-1]
    pageTotal = 405
    pageCount = 0

    while pageCount != pageTotal:
        pageCount += 1
        if pageCount == 1:
            chapter_url_list.append(book_url)
        else:
            chapter_url_list.append(base_url + str(pageCount))

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = code

    # print(response_1.text)

    book_title_regex = '<title>(.*).txt全文免费在线阅读_趣书网</title>'
    book_title = re.findall(book_title_regex, response_1.text)

    # pprint(chapter_url_list)
    print(book_title)


content = ""


def getContent(url):
    global content
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = code

    # print(response_2.text)

    content = response_2.text
    startIndex = content.find("<br>")
    endIndex = content.find(" </span>")
    content = content[startIndex:endIndex]
    if content == "":
        content = response_2.text
        startIndex = content.find("<br />")
        content = content[startIndex:endIndex]
        # print(startIndex)
    content = content.replace('<p>', '').replace('<br />', '').replace('<br>', '\n').replace('&bull;','•').replace('&nbsp;','').replace('&hellip;','…').replace('</p>','\n').replace('&lsquo;',"'").replace('&rsquo;',"'").replace("&ldquo;","“").replace("&rdquo;","”").replace("&mdash;","—").replace('\u3000',' ').replace('�','*')

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