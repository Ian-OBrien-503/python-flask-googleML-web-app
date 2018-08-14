#this class is derived from the base class and implements model using sqlite3
#I have not taken any database classes yet and know next to no SQL so i copied alot of the 
#logic from the flask slides to test the database to get it running

from Model import Model #importing parent class
import sqlite3

DB_FILE = 'entries.db' # database file

class model(Model):

  def __init__(self):
    #consturctor that creates db on startup if it does not exist
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    try:  cursor.execute("select count(rowid) from reviews")
    except sqlite3.OperationalError:
      cursor.execute("CREATE TABLE IF NOT EXISTS reviews (title TEXT,year_released TEXT,genre TEXT,rating TEXT,reviewer TEXT,comments TEXT)")
    cursor.close()

  def select(self):
    #gets all rows from the database containing complete review information
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM reviews")
    return cursor.fetchall()

  def insert(self, title, year_released, genre, rating, reviewer, comments):
    #inserts entry into the database (title, year_released, genre, rating, reviewer, comments)
    params = {'title':title, 'year_released':year_released, 'genre':genre, 'rating':rating, 'reviewer':reviewer, 'comments':comments}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO reviews (title, year_released, genre, rating, reviewer, comments) VALUES (:title, :year_released, :genre, :rating, :reviewer, :comments)", params)
    connection.commit()
    cursor.close()
    return True
