import os
import openai
from flask import Flask
from flask import render_template
from flask import request

openai.api_key = "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"


app = Flask(__name__)
@app.route("/", methods=['POST','GET'])
def hello_world():
    if request.method =='POST':
        response = openai.Completion.create(
            engine="davinci",
            prompt=request.form['msg'],
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        user_msg = request.form['msg'] + response["choices"][0]["text"]
    else:
        user_msg = "Create an outline for an essay about Walt Disney and his contributions to animation:\n\nI: Introduction"
    return render_template('hello.html', output_msg = user_msg)

app.run('0.0.0.0', port=4444, debug=True)


