"""
flask app english to french translator using GCP_ML_API 
"""
from flask import Flask, render_template, redirect, request, url_for, jsonify
from snippets import translate_text
from model import model

app = Flask(__name__)       #our Flask app
model = model()             #instantiating model class \
target1 = 'fr'              #for specifying translation to french

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
    model.insert(request.form['string'])
    model.fr_string = translate_text(target1, model.en_string)
    return render_template('done.html', model = model)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4997, debug = True)
