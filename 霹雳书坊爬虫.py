import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}
'''
https://m.pilibook.com/3/3816/629590.html
https://m.pilibook.com/3/3816/629591.html
'''
book_title = []
chapter_url_list = []

encoding = 'gbk'
def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'https://www.pilibook.com/4/4242/'
    base_url = 'https://www.pilibook.com/4/4242/'.replace(".html","")
    first_chapter_url = 687916
    last_chapter_url =  688008

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = encoding

    #print(response_1.text)

    book_title_regex = '<title>(.*)章节目录_耽美小说_霹雳书坊</title>'
    book_title = re.findall(book_title_regex, response_1.text)

    chapter_url_list = []
    for i in range(first_chapter_url,last_chapter_url+1):
        chapter_url_list.append(base_url+str(i)+'.html')


    pprint(chapter_url_list)
    #print(book_title)

content = ""
chapter_title = ""
def getContent(url):
    global content
    global chapter_title
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = encoding

    #print(response_2.text)

    article_regx = '<div id="novelcontent" class="novelcontent" style="word-break:break-all;">((.|\n)*)</p>'
    article = re.findall(article_regx, response_2.text)

    chapter_regx = '<h1 id="chaptertitle">(.*)</h1>'
    chapter = re.findall(chapter_regx, response_2.text)
    chapter_title = chapter[0]

    content = str(article[0]).replace('</p>', '\n').replace('<p>', '\n').replace("('\\r\\n\\t\\t ","\n").replace('�',"*").replace('\\u3000','')
    content = content[0:-7]

    #pprint(content)
    #print(chapter_title)

def export():
    save_path = book_title[0] + '.txt'
    count = 0

    with open(save_path, 'a+', encoding=encoding) as f:
        for x in chapter_url_list:
            getContent(x)

            f.write('\n'+ chapter_title + '\n')
            f.write(content + '\n')

            count += 1
            print('第{}章爬取完毕！'.format(count))


getChapters()
export()
