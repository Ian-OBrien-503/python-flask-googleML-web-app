"""
flask app for routing request to landing page and movie review page 
"""
from flask import Flask, render_template, redirect, url_for, request, jsonify
from Model import Model
from model_sqlite3 import model

app = Flask(__name__)       # our Flask app
model = model()             #instantiate dictionary
"""
Function decorator === app.route('/',index())
"""

#landing page for website
@app.route('/')
def index():
  return render_template('home.html') 
 
#this route will allow users to read all current reviews in the "database"
#had issues formating so used jsonify method
@app.route('/review', methods = ['GET'])
def review():
  return jsonify(model.select())

#this route will allow users to add reviews to the database via a form
#redirects to reviews page when completed 
@app.route('/post_review', methods = ['GET'])
def post_review():
    return render_template('index.html')

#this route handles the adding of the reviews and then redirects the user to all 
#of the reviews once completed
@app.route('/add_review', methods = ['POST'])
def add_review():
  model.insert(request.form['title'],request.form['year_released'],request.form['genre'],request.form['rating'],request.form['reviewer'],request.form['comments'])
  return redirect(url_for('review'))
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4996, debug = True)
