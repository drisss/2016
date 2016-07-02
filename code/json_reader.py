__author__ = 'driss'

import json, os.path
from pprint import pprint

fr_dir_path_groupA = "/home/driss/data/HAckaTal2016/Tweets/Matchs/train_euro2016/Groupe_A/fr/"
tweets_json = []


def readDir(dir_path):

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith("json") :
                for line in open(os.path.join(dir_path, file)) :
                    tweets_json.append(json.loads(line))


def read_json_file(file_path):
                for line in open(file_path) :
                    tweets_json.append(json.loads(line))
                    for tweet in tweets_json :
                        print(tweet['text'])

read_json_file(os.path.join(fr_dir_path_groupA , "Albanie_Suisse_2016-06-11_15h_fr.json"))
