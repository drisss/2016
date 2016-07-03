__author__ = 'driss'


#!/usr/bin/python
# coding: utf-8

import os.path, codecs, io
from Tweet import Tweet
from Team import Team
from Preprocess import token_name, get_players_in_tweet, get_teams_in_tweet, remove_accents

from Player import Player

def containTeam(teams, team_name):
    is_in = 0
    for current_team in teams:
        if current_team.name == team_name:
            is_in = 1
    return is_in

def read_tsv_tweet_file(tweet_file_path,players_file_path):
    tweets = []
    teams = []
    players = read_tsv_player_file(players_file_path)

    for player in players :
        if containTeam(teams, player.team) == 0 :
            team = Team(player.team)
            teams.append(team)

    print("teams size: ", len(teams))

    for line in open(tweet_file_path) :
        line = line.replace("\r\n","\n").replace('\r','\n')
        print(line)
        tab = line.lower().split("\t")
        id = tab[0]
        date = tab[1]
        text = tab[2]
        tweet_players = get_players_in_tweet(text,players)
        tweet_teams = get_teams_in_tweet(text,teams)
        nb_retweet = tab[3]
        lang = tab[4]
        tweet = Tweet(id,date,text,tweet_players, tweet_teams, nb_retweet,lang)

        tweets.append(tweet)

    return tweets


def read_tsv_player_file(file_path):
    players = []
    for line in codecs.open(file_path,"r","utf-8") :
        line = line.replace('\n','')
        tab = line.lower().split("\t")
        firstname = tab[0]
        lastname = tab[1]
        function = tab[2]
        team = tab[3]
        player = Player(firstname,lastname,function,team)
        players.append(player)
    return players
