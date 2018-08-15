"""
flask app english to french translator using GCP_ML_API 
"""
from flask import Flask, render_template, redirect, request, url_for, jsonify
from model import model
from snippets import translate_text
from google.cloud import translate
import six
import argparse

app = Flask(__name__)       #our Flask app
model = model()             #instantiating model class \
target1 = 'fr'              #for specifying translation to french
target2 = 'it'              #for specifying translation to italian

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

#this function will handle the translation from english string to french string via google
#translate ML_API
@app.route('/ML_transform', methods = ['POST'])
def ML_transform():
    model.insert_en(request.form['string'])
    model.insert_fr(translate_text(target1, model.en_string))
    model.insert_it(translate_text(target2, model.en_string))

    return render_template('done.html', model = model)

#specify what port to run on, running on port 4997 because i seem to have probelms with 8000 all of the time
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4996, debug = True)
