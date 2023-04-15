
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.
client = MongoClient('localhost', 27017)
db = client.google_map

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/matjip', methods=["GET"])
# def get_matjip():
#     # gu_receive 라는 변수에 전달받은 구 이름을 저장합니다.
#     # 구 이름에 해당하는 모든 맛집 목록을 불러옵니다. 
#     # matjip_list 라는 키 값에 맛집 목록을 담아 클라이언트에게 반환합니다.
#     return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=4444,debug=True)
