#this class will store the various translations that will be used
#in html form to print to a webpage

from flask import Flask, request

class model():
    def __init__(self):
        self.en_string = ""
        self.fr_string = ""
        pass

    def insert_en(self, string):
        self.en_string = string
        pass

    def insert_fr(self, string):
        self.fr_string = string
        pass
