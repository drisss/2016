__author__ = 'driss'



import datetime

class Team:


    def __init__(self, name):

        self.name = name

    def print_team(self):
        print(self.name)

    def getName(self):
        return self.name
