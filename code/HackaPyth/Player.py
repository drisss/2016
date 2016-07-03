__author__ = 'driss'


import datetime
from Team import Team
class Player:


    def __init__(self, firstname, lastname, function, team, nickname):

        self.firstname = firstname
        self.lastname = lastname
        self.function = function
        self.team = team
        self.nickname = nickname


    def print_player(self):
        print(self.firstname ,self.lastname,self.function ,self.team)

    def getFirstName(self):
        return self.firstname


    def getLastName(self):
        return self.lastname


    def getNickName(self):
        return self.nickname
