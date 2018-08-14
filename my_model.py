"""
movie review data is stored in the model class and is stored in a python dictionary for hw#2
"""

class model():
    def __init__(self):
    #this constructuor initalizes all of the data for the movie reviews for hw#2, it is a dictionary of list
        self.movie_dict = {'Die Hard' : [1990, 'action', '5 stars', 'Ian O.','Bruce Willis at his best!'],
                           'Signs'    : [2000, 'sci-fi', '1 star', 'everybody', 'M. Night\'s worst film'],
                           'Heriditary' : [2018, 'horror', '4 stars', 'my cat', 'made my tail stand straight up! meow!']}        
