# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import requests
from bs4 import BeautifulSoup
from dasandao import DasanDAO
from konlpy.utils import pprint

class NaverCrawler(object):
    def __init__(self, dasandao, urls):
        self.dasandao = dasandao
        self.urls = urls

    # 네이버지식인에 있는 해당년도와 페이지를 입력
    def crawl_link(self):
        year = 2016
        pages = 226

        for page in range(1,pages):
            page = str(page)
            link = urls.format(year,page)

            self.crawling(link)

    # 크롤링
    def crawling(self, link):
        res = requests.get(link)
        soup = BeautifulSoup(res.content)

        #질문 크롤링
        quest = []
        val = []
        titles = soup.find_all('td', attrs = {'class':'title'})

        for title in titles:
            title = title.get_text()
            quest.append(title)

        # regular_expression 으로 "re:" 부분을 제거
        for i in quest:
            val.append(re.sub('\w+:','',i))

        # 크롤링 한것의 공백제거
        for question in val:
            question = question.strip()
            pprint (question)

        #디렉토리 크롤링
        direct = []
        classifys = soup.find_all('td', attrs = {'class':'field'})
        for classify in classifys:
            direct.append(classify.get_text())

        # 네이버지식인 사이트자체만의 코드로 인해서 원하는결과를 뽑기위해서 짝수만 크롤링
        for i in range(1,40,2):
            directory = direct[i]
            pprint (directory)

        # dasando.py로 question과 directory 인자를 넘김
        self.dasandao.dasan_db(str(question), str(directory))

# 네이버지식인 사이트주소
urls = 'http://kin.naver.com/userinfo/answerList.nhn?userId=dasan_120&year={}&page={}'

if __name__ == '__main__':
    dasandao = DasanDAO()
    crawler = NaverCrawler(dasandao, urls)
    crawler.crawl_link()
