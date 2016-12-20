# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, jsonify
from dasandao import DasanDAO
from machine_learning import Machine
from answering import Answer
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def hello_json():
    data = {'name' : 'Kyeoung Soo', 'family' : 'Kim'}
    return jsonify(data)

# dasandao에서 select_in_question함수 호출
@app.route('/question/search/<keyword>')
def search_news(keyword):
    dasandao = DasanDAO()
    data = dasandao.select_in_question(str(keyword))
    return jsonify(data)

# machine_learning 에서 model를 만든후, answering에서 answer_bot함수 호출
@app.route('/question/answer/<keyword>')
def answer(keyword):
    # model
    machine = Machine()
    trained = machine.training()

    #answer
    answer = Answer(trained)
    data = answer.answer_bot(keyword)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
