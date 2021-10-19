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

def player_submit():
    
    user_input = request.args
    
    X_test = user_input['player_name']
    
    salary = pickle.load(open('../model/salary_model.pkl', 'rb'))
    



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)