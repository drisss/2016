import datetime

class Tweet:

    def __init__(self, id, date, text, players, teams, nb_retweet,lang):

        self.id = id
        self.date = date
        self.text = text
        self.players = players
        self.teams = teams
        self.nb_retweet = nb_retweet
        self.lang = lang



    def print_tweet(self):
        print(self.id,self.date,self.text,self.players, self.teams, self.nb_retweet,self.lang)

    def getId(self):
        return self.__id

    def setX(self, id):
        self.__id = id


    def getText(self):
        return self.text

    def setX(self, text):
        self.__text = text