__author__ = 'driss'
import os
from Tweet import Tweet
from Player import Player
from TSVreader import read_tsv_player_file, read_tsv_tweet_file


tweets_with_no_player = []
tweets_with_a_team_no_player = []
tweets_with_single_players = []
tweets_with_two_players = []
tweets_with_many_players = []


tweets = read_tsv_tweet_file(os.path.join("France_Roumanie_2016-06-10_21h_fr.json.tsv"))

for tweet in tweets :
    tweet.print_tweet()

players = read_tsv_player_file(os.path.join("list_players"))
teams = set()

#for player in players :
#    player.print_player()
#    teams.add(player.team)


def cluster_tweets(tweets) :
    for tweet in tweets :
        nb_players =  containPlayer(tweet.getText())
        if nb_players == 0 :
            if (containTeam(tweet.getText()) > 0) :
                tweets_with_a_team_no_player.append(tweet)
            else :
                tweets_with_no_player.append(tweet)

        elif nb_players == 1 :
            tweets_with_single_players.append(tweet)
        elif nb_players == 2 :
            tweets_with_two_players.append(tweet)
        else :
            tweets_with_many_players.append(tweet)


def containPlayer( text) :
    nb_players = 0
    for player in players :

        if (player.getFirstName() in text.lower()) or (player.getLastName() in text.lower()) :
            nb_players = nb_players + 1
    return nb_players

def containTeam(text) :
    nb_teams = 0
    for team in teams :

        if (team in text.lower()) or (team in text.lower()) :
            nb_teams = nb_teams + 1
    return nb_teams

#cluster_tweets(tweets)

#print("tweets_with_a_team_no_player:", tweets_with_a_team_no_player.__len__())
#print("tweets_with_no_player :",tweets_with_no_player.__len__())
#print("tweets_with_single_players: ", tweets_with_single_players.__len__())
#print("tweets_with_two_players:",tweets_with_two_players.__len__())
#print("tweets_with_many_players:", tweets_with_many_players.__len__())