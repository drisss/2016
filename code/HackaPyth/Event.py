__author__ = 'driss'

class Event:

    def __init__(self, type, terms, nb_players, nb_teams):

        self.type = type
        self.terms = terms
        self.nb_players = nb_players
        self.nb_teams = nb_teams

    def print_event(self):
        print(self.type, self.terms, self.nb_players, self.nb_teams)


    def getType(self):
        return self.type

    def getTerms(self):
        return self.terms

    def getNbPlayers(self):
        return self.nb_players

    def getNbTeams(self):
        return self.nb_teams

    def addTerm(self, term):
        self.terms.append(term)
