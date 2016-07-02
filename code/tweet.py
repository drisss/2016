import datetime

class tweet:

    """Classe définissant un tweet caractérisée par :
    son text """


    def __init__(self, date, text,nb_retweet): # Notre méthode constructeur

        self.date = date
        self.text = text
        self.nb_retweet = nb_retweet


    def print_tweet(self):
        print(self.date,self.text)