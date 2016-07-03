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

        list_param = [self.id, self.date, self.text, self.nb_retweet, self.lang]
        csv_wr = csv.writer(f, delimiter='\t')
        csv_wr.writerow(list_param)

    def print_in_tsv_annot(self, f, event):
        if len(self.players) == 0:
            if len(self.teams) == 0:
                list_param = [self.date, event.type]
            else:
                list_param = [self.date, event.type, self.teams[0]]
        elif len(self.players) == 1:
            list_param = [self.date, event.type, self.getPlayer1()]
        else:   # len(self.players) == 2:
            p = self.getPlayer1() + " ; " + self.getPlayer2()
            list_param = [self.date, event.type, p]

        csv_wr = csv.writer(f, delimiter='\t')
        csv_wr.writerow(list_param)

    def getPlayer1(self):
        return self.players[0]

    def getPlayer2(self):
        return self.players[1]

    def getText(self):
        return self.text

    def setX(self, text):
        self.__text = text