__author__ = 'driss'


import datetime

class Player:


    def __init__(self, firstname, lastname, function, team):

        self.firstname = firstname
        self.lastname = lastname
        self.function = function
        self.team = team


    def print_player(self):
        print(self.firstname ,self.lastname,self.function ,self.team)

    def getFirstName(self):
        return self.firstname


    def getLastName(self):
        return self.lastname

