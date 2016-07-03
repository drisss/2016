#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import re
import codecs
from nltk.tokenize import TweetTokenizer
import unicodedata

__author__ = 'driss'


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def token_name(name):
    last_name = remove_accents(name)
    # last_name = re.sub(u'[éèêë]', "e",name.lower(), flags=re.I)
    # last_name = re.sub(u'[àâä]',"a",last_name, flags=re.I)
    # last_name = re.sub(u'[ùûü]',"u",last_name, flags=re.I)
    # last_name = re.sub(u'[ìîï]',"i",last_name, flags=re.I)
    # last_name = re.sub(u'[òôö]',"o",last_name, flags=re.I)
    return last_name.tolower()


def get_players_in_tweet(tweet, players):
    tweet_players = []

    list_token = tknzr.tokenize(tweet)

    for token in list_token:
        # line = line[:-1]
        last_name = remove_accents(token)
        last_name = last_name.tolower()

        last_name = re.sub(r'([^aeuiyo])([aeuiyo])[aeuiyo]+([^aeuiyo]*)$',
                           r'\g<1><2><3>', last_name, flags=re.I)

        for player in players:
            if last_name in player.getLastName():
                tweet_players .append(player)

    return tweet_players


def get_teams_in_tweet(tweet, teams):
    tweet_teams = []

    list_token = tknzr.tokenize(tweet)

    for token in list_token:
        # line = line[:-1]
        name = remove_accents(token)
        name = name.tolower()
        name = re.sub(r'([^aeuiyo])([aeuiyo])[aeuiyo]+([^aeuiyo]*)$',
                      r'\g<1><2><3>', name, flags=re.I)

        for team in teams:
            if name in team.getName():
                tweet_teams.append(team)

    return tweet_teams


if __main__ == "__main__":

    f_tweets = codecs.open(sys.argv[2], "r", "utf-8")
    f_out = codecs.open(sys.argv[3], "w", "utf-8")
    count_per = 0
    sentence = ""

    tknzr = TweetTokenizer()
