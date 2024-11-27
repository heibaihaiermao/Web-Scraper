import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}
'''
http://www.yuzhaiwu520.org/8_8909/1049802.html
http://www.yuzhaiwu520.org/8_8909/1049575.html'''
book_title = []
chapter_url_list = []

encoding = 'gbk'
def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'http://www.yuzhaiwu520.org/8_8909/'
    base_url = 'http://www.yuzhaiwu520.org/8_8909/.html'.replace(".html","")
    first_chapter_url = 1049575
    last_chapter_url = 1049802

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = encoding

    #print(response_1.text)

    book_title_regex = '<meta property="og:novel:book_name" content="(.*)"/>'
    book_title = re.findall(book_title_regex, response_1.text)

    chapter_url_list = []
    for i in range(first_chapter_url,last_chapter_url+1):
        chapter_url_list.append(base_url+str(i)+'.html')


    #pprint(chapter_url_list)
    print(book_title)

content = ""
def getContent(url):
    global content
    global chapter_title
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = encoding

    #print(response_2.text)

    article_regx = '<div id="content">((.|\n)*)<div class="bottem2">'
    article = re.findall(article_regx, response_2.text)

    content = str(article[0]).replace('&nbsp;&nbsp;&nbsp;&nbsp;', '').replace('<br />', '\n').replace("\\r\\n","").replace("</div>\\t\\t\\t\\t'",'').strip("()")
    content = content[0:-7]

    #pprint(content)

def export():
    save_path = book_title[0] + '.txt'
    count = 0

    with open(save_path, 'a+', encoding=encoding) as f:
        for x in chapter_url_list:
            getContent(x)

            f.write(content + '\n')

            count += 1
            print('第{}章爬取完毕！'.format(count))


getChapters()
export()