import requests
from bs4 import BeautifulSoup
import pandas as pd

# 키워드와 URL 설정
keyword = '비트코인'
url = f'https://search.naver.com/search.naver?where=news&query={keyword}'

# 웹 페이지 요청 및 파싱
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 제목, 링크, 매체명 추출
articles = soup.select('.news_tit')
press_names = soup.select('.info_group .press')  # 뉴스 매체 이름 추출

# 데이터 수집
news_data = [
    {
        'title': article.text,
        'link': article['href'],
        'press': press.text if press else 'Unknown'
    }
    for article, press in zip(articles, press_names)
]

# 데이터프레임 생성
df_news = pd.DataFrame(news_data)

# 데이터 출력 (최상위 5개)
print(df_news.head())

