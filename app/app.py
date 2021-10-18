"""
Modified from https://github.com/tatiblockchain/python-deep-learning-chatbot
Modified from Lesson 5.4
"""

# Libraries Used
from flask import Flask, render_template, jsonify, request, Response
import pickle

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])


        
    
@app.route('/messenger', methods=["GET", "POST"])
def messenger ():
    return render_template('chatbot.html', **locals())

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)