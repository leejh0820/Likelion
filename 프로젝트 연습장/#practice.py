#practice
import requests
import pprint
import urllib.parse
import time
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db= client.google_map

city = ["Berkeley"]

def get_google_result(keyword):
    time.sleep(0.1)
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={keyword}&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=AIzaSyCcvW8a-l-tXtMKVwuu_5syXQdDRAvb3L0"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response['name']

docs = []
for gu in city:
    # '강님구 맛집', '종로구 맛집', '용산구 맛집' .. 을 반복해서 인코딩합니다.
    keyword = f'{gu} 맛집'
    # 맛집 리스트를 받아옵니다.
    matjip_list = get_google_result(keyword)

    # 구별 맛집 구분선입니다.
    print("*"*80 + gu)

    for matjip in matjip_list:
        # 구 정보를 추가합니다.
        matjip['gu'] = gu
        # 맛집을 인쇄합니다.
        pprint.pprint(matjip)
        # docs에 맛집을 추가합니다.
        docs.append(matjip)



db.matjip.insert_many(docs)

# def get_naver_result(keyword):
#     time.sleep(0.1)
#     # url에 전달받은 검색어를 삽입합니다.
#     api_url = f"https://openapi.naver.com/v1/search/local.json?query={keyword}&display=10&start=1&sort=random"
#     # 아이디와 시크릿 키를 부가 정보로 같이 보냅니다.
#     headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
#     # 검색 결과를 data에 저장합니다.
#     data = requests.get(api_url, headers=headers)
#     # 받아온 JSON 결과를 딕셔너리로 변환합니다.
#     data = data.json()
#     return data['items']
