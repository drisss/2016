__author__ = 'driss'

import os.path
from Tweet import Tweet
from Preprocess import token_name, get_players_in_tweet, get_teams_in_tweet

from Player import Player
tweets = []

def readDir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith("json.tsv") :
                for line in open(os.path.join(dir_path, file)) :
                    tweets.append(line)


def read_tsv_tweet_file(file_path):
    tweets = []
    for line in open(file_path) :
        tab = line.lower().split("\t")
        id = tab[0]
        date = tab[1]
        text = tab[2]
        players = get_players_in_tweet(text)
        teams = get_teams_in_tweet(text)
        nb_retweet = tab[3]
        lang = tab[4]
        tweet = Tweet(id,date,text,nb_retweet,lang)
        tweets.append(tweet)
    return tweets


def read_tsv_player_file(file_path):
    players = []
    for line in open(file_path) :
        line = line.replace('\n','')
        tab = line.lower().split("\t")
        firstname = tab[0]
        lastname = token_name(tab[1])
        function = tab[2]
        team = tab[3]
        player = Player(firstname,lastname,function,team)
        players.append(player)
    return players
