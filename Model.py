#this is the base class that will be used for an entry in the data base

class Model():

  def select(self):
  #gets all entries from the database
  #returns list w/ all rows/entries from database
    pass

  def insert(self, title, year_released, genre, rating, reviewer, comments):
  #inserts parameters into database as an entry
    """:title: string"""
    """:year_released: int"""
    """:genre: string"""
    """:rating: string"""
    """:reviwer: string"""
    """:comments: string"""
    pass
