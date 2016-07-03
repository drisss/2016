import os
# from Tweet import Tweet
# from Player import Player
# from Event import Event
from TSVreader import read_tsv_player_file, read_tsv_tweet_file, read_tsv_events_file
import time
from nltk.tokenize import TweetTokenizer


clustered_tweets_dir = "../../Data/clustered_tweets/"

__author__ = 'driss'


def print_tweets_annotation(match_dirpath):

    match_fnames = [f for f in os.listdir(os.path.join(match_dirpath))
                    if not f.startswith('.')]   # Remove hidden files

    for match_fname in match_fnames:
        match_fpath = os.path.join(match_dirpath, match_fname)

        players = read_tsv_player_file("list_players.tsv", match_fpath)

        events = read_tsv_events_file("../../Data/events/event_types.tsv")

        only_team_events = [x for x in events
                            if (x.getNbPlayers() == '0' and
                                x.getNbTeams() == '1')]
        no_player_events = [x for x in events if x.getNbPlayers() == '0']
        one_player_events = [x for x in events if x.getNbPlayers() == '1']
        two_player_events = [x for x in events if x.getNbPlayers() == '2']

        no_player_tweets = \
            read_tsv_tweet_file(os.path.join(match_dirpath, "no_player_tweets.tsv"), players)
        only_team_tweets = \
            read_tsv_tweet_file(os.path.join(match_dirpath, "only_team_tweets.tsv"), players)
        one_player_tweets = \
            read_tsv_tweet_file(os.path.join(match_dirpath, "one_player_tweets.tsv"), players)
        two_players_tweets = \
            read_tsv_tweet_file(os.path.join(match_dirpath, "two_players_tweets.tsv"), players)

        # tweets_with_many_players = read_tsv_tweet_file(os.path.join(clusetered_tweet_fpath,match_fpath, "tweets_with_many_players.tsv"), players)

        smart(one_player_tweets, one_player_events)


def smart(tweets, events):
    for tweet in tweets:
        found_event_types = contain_event(tweet, events)
        if len(found_event_types) > 0:
            print(found_event_types)


def contain_event(tweet, events):
    type_freq = dict()
    tknzr = TweetTokenizer()
    list_token = tknzr.tokenize(tweet.getText())

    for event in events:
        event_terms = event.getTerms()
        # print(event_terms)
        for term in event_terms:
            if term in list_token:
                if event.getType() not in type_freq.keys():
                    type_freq[event.getType()] = 1
                else:
                    type_freq[event.getType()] += 1

    return type_freq


def parse_clustered_tweet(clustered_tweets_dir):

    dirname_lst = [f for f in os.listdir(clustered_tweets_dir)
                   if not f.startswith('.')]  # Remove hidden files

    print(dirname_lst)

    for dirname in dirname_lst:
        match_dirpath = os.path.join(clustered_tweets_dir, dirname)

        print_tweets_annotation(match_dirpath)


if __name__ == "__main__":

    start_time = time.time()

    # parse_dir_match('../../Data/match')

    parse_clustered_tweet(clustered_tweets_dir)

    print("--- %s seconds ---" % (time.time() - start_time))
