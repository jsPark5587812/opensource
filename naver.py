import requests
from bs4 import BeautifulSoup
import pandas as pd


def start():
    # 키워드, URL
    keyword = '비트코인'
    url = f'https://search.naver.com/search.naver?where=news&query={keyword}'

    # 웹 페이지 요청
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # news_tit 부분 필터링
    articles = soup.select('.news_tit')
    print( articles )

    # 뉴스 제목 확인
    article = articles[0]
    title = article.text
    print ( title )
    # 뉴스 제목 데이터프레임 생성
    title_tot = pd.DataFrame([article.text for article in articles], columns=['title'])
    print( title_tot.head())


start() 
