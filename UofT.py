import requests  # 导入用于发送请求的库
import re  # 导入筛选出小说内容的库
from pprint import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'referer': 'https://www.google.com/',
}

book_title = []
chapter_url_list = []
code = "UTF-8"

def getChapters():
    global book_title
    global chapter_url_list

    book_url = 'https://artsci.calendar.utoronto.ca/search-programs?combine=&type=All&field_subject_area_prog_search_value=Computer+Science'

    session = requests.Session()
    response_1 = session.get(book_url, headers=headers)
    response_1.encoding = code

    pprint(response_1.text)

    program_title_regex = '<h3 class="js-views-accordion-group-header"><div aria-label="(.*)">'
    program_titles = re.findall(program_title_regex, response_1.text)

    courses_regex = '<h3 class="js-views-accordion-group-header"><div aria-label="(.*)">'


    pprint(program_titles)
    print(len(program_titles))


content = ""


def getContent(url):
    global content
    session = requests.Session()
    response_2 = session.get(url, headers=headers)
    response_2.encoding = code

    # print(response_2.text)

    article_regx = '<p>(.*)</p><p></p>'
    article = re.findall(article_regx, response_2.text)
    content = article[0].replace('</p><p>', '\n\n').replace("�"," ")

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