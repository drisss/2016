import csv


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
        print(self.date, self.text, self.players, self.teams)
        for player in self.players:
            player.print_player()
        for team in self.teams:
            team.print_team()

    def print_in_tsv_file(self, f):

        list_param = [self.date, self.text, self.nb_retweet, self.lang]
        csv_wr = csv.writer(f, delimiter='\t')
        csv_wr.writerow(list_param)

    def getId(self):
        return self.__id

    def setX(self, id):
        self.__id = id

    def getText(self):
        return self.text

    def setX(self, text):
        self.__text = text