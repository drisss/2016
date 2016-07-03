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

        fname_lst = [f for f in os.listdir(os.path.join(match_dirpath))]

        for fname in fname_lst:
            match_fpath = os.path.join(match_dirpath, fname)

            players = read_tsv_player_file("list_players.tsv", match_fpath)

            events = read_tsv_events_file("../../Data/events/event_types.tsv")

            only_team_events = [x for x in events
                                if (x.getNbPlayers() == '0' and
                                    x.getNbTeams() == '1')]
            no_player_events = [x for x in events if x.getNbPlayers() == '0']
            one_player_events = [x for x in events if x.getNbPlayers() == '1']
            two_player_events = [x for x in events if x.getNbPlayers() == '2']

            match_dirname = os.path.basename(os.path.join(match_dirpath))
            match_basename = os.path.splitext(match_dirname)[0]
            team_names = match_basename.lower().split('_')[:2]

            tweets_with_no_player = \
                read_tsv_tweet_file(os.path.join(match_dirpath, "tweets_with_no_player.tsv"), players)
            tweets_with_a_team_no_player = \
                read_tsv_tweet_file(os.path.join(match_dirpath, "tweets_with_a_team_no_player.tsv"), players)
            tweets_with_single_players = \
                read_tsv_tweet_file(os.path.join(match_dirpath,"tweets_with_single_players.tsv"),players)
            tweets_with_two_players = \
                read_tsv_tweet_file(os.path.join(match_dirpath,"tweets_with_two_players.tsv"),players)

            # tweets_with_many_players = read_tsv_tweet_file(os.path.join(clusetered_tweet_fpath,match_fpath,"tweets_with_many_players.tsv"),players)

            for tweet in tweets_with_single_players:
                    found_types = contain_event(tweet,one_player_events)
                    if len(found_types) > 0:
                        print(found_types)


def parse_clustered_tweet(clustered_tweets_dir):

    dirname_lst = [f for f in os.listdir(clustered_tweets_dir)]

    print(dirname_lst)

    for dirname in dirname_lst:
        match_dirpath = os.path.join(clustered_tweets_dir, dirname)

        print_tweets_annotation(match_dirpath)


def contain_event(tweet, events):
    found_types = []
    tknzr = TweetTokenizer()
    list_token = tknzr.tokenize(tweet.getText())

    for event in events:
        event_terms = event.getTerms()
        # print(event_terms)
        for term in event_terms:
            if term in list_token:
                found_types.append(event.getType())
    return found_types


if __name__ == "__main__":

    start_time = time.time()

    # parse_dir_match('../../Data/match')

    parse_clustered_tweet(clustered_tweets_dir)

    print("--- %s seconds ---" % (time.time() - start_time))
