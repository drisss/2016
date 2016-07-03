__author__ = 'driss'

#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import codecs
from nltk.tokenize import TweetTokenizer


list_player={}

def token_name(name):

    last_name = re.sub(u'[éèêë]',"e",name.lower(), flags=re.I)
    last_name = re.sub(u'[àâä]',"a",last_name, flags=re.I)
    last_name = re.sub(u'[ùûü]',"u",last_name, flags=re.I)
    last_name = re.sub(u'[ìîï]',"i",last_name, flags=re.I)
    last_name = re.sub(u'[òôö]',"o",last_name, flags=re.I)
    return last_name

f_tweets = codecs.open(sys.argv[2], "r", "utf-8")
f_out = codecs.open(sys.argv[3], "w", "utf-8")
count_per = 0
sentence = ""

tknzr = TweetTokenizer()


def get_players_in_tweet(tweet, players):
    tweet_players = []

    list_token = tknzr.tokenize(tweet)

    for token in list_token:
        #line = line[:-1]

            last_name = re.sub(r'[éèêë]',"e",token.lower(), flags=re.I)
            last_name = re.sub(r'[àâä]',"a",last_name, flags=re.I)
            last_name = re.sub(r'[ùûü]',"u",last_name, flags=re.I)
            last_name = re.sub(r'[ìîï]',"i",last_name, flags=re.I)
            last_name = re.sub(r'[òôö]',"o",last_name, flags=re.I)
            #last_name = re.sub(r'[aeuiyo]+([^aeuiyo]*)$',r'\g<1>', last_name, flags=re.I)
            last_name = re.sub(r'([^aeuiyo])([aeuiyo])[aeuiyo]+([^aeuiyo]*)$',r'\g<1><2><3>', last_name, flags=re.I)

            for player in players :
                if last_name in player.getLastName():
                    tweet_players .append(player)
    return tweet_players


def get_teams_in_tweet(tweet, teams):
    tweet_teams = []

    list_token = tknzr.tokenize(tweet)

    for token in list_token:
        #line = line[:-1]

            name = re.sub(r'[éèêë]',"e",token.lower(), flags=re.I)
            name = re.sub(r'[àâä]',"a",name, flags=re.I)
            name = re.sub(r'[ùûü]',"u",name, flags=re.I)
            name = re.sub(r'[ìîï]',"i",name, flags=re.I)
            name = re.sub(r'[òôö]',"o",name, flags=re.I)
            #last_name = re.sub(r'[aeuiyo]+([^aeuiyo]*)$',r'\g<1>', last_name, flags=re.I)
            name = re.sub(r'([^aeuiyo])([aeuiyo])[aeuiyo]+([^aeuiyo]*)$',r'\g<1><2><3>', name, flags=re.I)

            for team in teams :
                if name in team.getName():
                    tweet_teams.append(team)
    return tweet_teams

