
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)

# URL 별로 함수명이 같거나,
# route('/') 등의 주소가 같으면 안됩니다.
client = MongoClient('localhost', 27017)
db = client.bird_comming

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/message', methods = ['POST'])
def set_message():
    username_receive = request.form['username_give']
    contents_receive = request.form['contents_give']

    doc = {
        'username': username_receive,
        'contents': contents_receive,
        'created_at': datetime.now()
    }
    db.messages.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '메시지 작성에 성공했습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=4444, debug=True)
