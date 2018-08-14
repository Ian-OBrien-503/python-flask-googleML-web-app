"""
flask app english to french translator using GCP_ML_API 
"""
from flask import Flask, render_template, redirect, request, url_for, jsonify
from my_model import model

app = Flask(__name__)       #our Flask app
model = model()             #instantiate dictionary

#home page for website 
@app.route('/')
def index():
    return render_template('home.html')

#this page will prompt user to type their sentence in english that they wish to
#translate to french, it will be sent to translator GCP_ML_API and spit out
#the french translation
@app.route('/form', methods = ['GET'])
def form():
    return render_template('form.html')

@app.route('/ML_transform')
def ML_transform():
    return "ok"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4996, debug = True)
