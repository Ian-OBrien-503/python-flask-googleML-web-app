"""
flask app for routing request to landing page and movie review page 
"""
from flask import Flask, render_template, jsonify
from my_model import model

app = Flask(__name__)       # our Flask app
model = model()             #instantiate dictionary
"""
Fnction decorator === app.route('/',index())
"""
@app.route('/')
def index():
    #"""landing page"""
    return "A PLACE FOR MOVIE REWIVEWS...an experiment in web development" 
 
@app.route('/review')
def review():
   #publish reviews to webpage
   #this function will allow the reivews to be printed/published on the web app
    return render_template('layout.html', model = model) 



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4996) 
