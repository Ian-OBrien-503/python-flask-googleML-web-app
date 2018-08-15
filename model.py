#this class will store the various translations that will be used
#in html form to print to a webpage

from flask import Flask, request

class model():
    #constructor
    def __init__(self):
        self.en_string = ""
        self.fr_string = ""
        self.it_string = ""
        pass

    #used to insert english string into model
    def insert_en(self, string):
        self.en_string = string
        pass

    #used to insert french string into model
    def insert_fr(self, string):
        self.fr_string = string
        pass

    #used to insert italian string into model
    def insert_it(self, string):
        self.it_string = string
        pass
