#!/usr/bin/python
# coding: utf-8

import os.path, codecs, io
from Tweet import Tweet
from Team import Team
from Preprocess import token_name, get_players_in_tweet, get_teams_in_tweet, remove_accents

from Player import Player

__author__ = 'driss'


def containTeam(teams, team_name):
    is_in = 0
    for current_team in teams:
        if current_team.name == team_name:
            is_in = 1
    return is_in


def read_tsv_tweet_file(tweet_file_path,players):
    tweets = []
    teams = []

    for player in players :
        if containTeam(teams, player.team) == 0 :
            team = Team(player.team)
            teams.append(team)

    # print("teams size: ", len(teams))
    nb_line = 0
    for line in open(tweet_file_path):

        nb_line += 1
#        line = line.replace("\r\n","\n").replace('\r','\n')
        # line = remove_accents(line)
        # print(line)   # DEBUG
        tab = line.lower().strip().split("\t")
        id = tab[0]
        date = tab[1]
        text = tab[2]
        tweet_players = get_players_in_tweet(text, players)
        tweet_teams = get_teams_in_tweet(text, teams)
        nb_retweet = tab[3]
        lang = tab[4]
        tweet = Tweet(id, date, text, tweet_players, tweet_teams, nb_retweet, lang)
        tweets.append(tweet)
        # if nb_line > 100:    # DEBUG
        #     break

    return tweets


def read_tsv_player_file(player_fpath, match_fpath):
    players = []

    match_fname = os.path.basename(match_fpath)
    match_basename = os.path.splitext(match_fname)[0]
    team_names = match_basename.lower().split('_')[:2]

    # print(team_names)   # DEBUG

    for line in codecs.open(player_fpath, 'r', 'utf-8'):
        line = line.replace('\n', '')
        tab = line.lower().split('\t')

        team = tab[3]

        if team in team_names:
            firstname = tab[0]
            lastname = tab[1]
            function = tab[2]
            if len(tab) == 5:
                nickname = tab[4]
            else:
                nickname = "no_nickname"

            player = Player(firstname, lastname, function, team, nickname)
            players.append(player)

    return players
