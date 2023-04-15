
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.google.com/maps/search/restuarants/@37.8653588,-122.2759346,15z/data=!3m1!4b1!4m4!2m3!5m1!4e3!6e5',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.




soup = BeautifulSoup(data.text, 'html.parser')

restaurants = soup.select('#body-content > div.newest-list > div ')

# movies (tr들) 의 반복문을 돌리기
for restaurant in restaurants:
    # movie 안에 a 가 있으면,
    title = restaurants.select_one('h3.section>result>title')
    if title is not None:
        # a의 text를 찍어본다.
        print (title.text)

#############################
# (입맛에 맞게 코딩)
#############################
