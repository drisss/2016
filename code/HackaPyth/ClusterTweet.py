import os
# from Tweet import Tweet
# from Player import Player
# from Event import Event
from TSVreader import read_tsv_player_file, read_tsv_tweet_file  # read_tsv_events_file
import time
# from nltk.tokenize import TweetTokenizer

__author__ = 'driss'


clustered_tweets_dir = "../../Data/clustered_tweets/"


def print_cluster_tweets(tweets, match_fpath):

    match_fname = os.path.basename(match_fpath)
    match_basename = os.path.splitext(match_fname)[0]
    team_names = match_basename.lower().split('_')[:2]

    # TODO: complete country name

    dir_team = team_names[0] + '_' + team_names[1]
    team_dirpath = os.path.join(clustered_tweets_dir, dir_team)

    if not os.path.exists(team_dirpath):
        os.makedirs(team_dirpath)

    no_player_tweets = []
    only_team_tweets = []
    one_player_tweets = []
    two_players_tweets = []
    many_players_tweets = []

    for tweet in tweets:
        if len(tweet.players) == 0:
            if len(tweet.teams) == 1:
                only_team_tweets.append(tweet)
            else:
                no_player_tweets.append(tweet)

        elif len(tweet.players) == 1:
            one_player_tweets.append(tweet)

        elif len(tweet.players) == 2 and (tweet.getPlayer1().getTeam() == tweet.getPlayer2().getTeam()):
            two_players_tweets.append(tweet)
        else:
            many_players_tweets.append(tweet)

    print("only_team_tweets:", len(only_team_tweets))
    print("no_player_tweets :", len(no_player_tweets))
    print("one_player_tweets: ", len(one_player_tweets))
    print("two_players_tweets:", len(two_players_tweets))
    print("many_players_tweets:", len(many_players_tweets))

    print_tweets_in_file(no_player_tweets, os.path.join(team_dirpath, "no_player_tweets.tsv"))
    print_tweets_in_file(only_team_tweets, os.path.join(team_dirpath, "only_team_tweets.tsv"))
    print_tweets_in_file(one_player_tweets, os.path.join(team_dirpath, "one_player_tweets.tsv"))
    print_tweets_in_file(two_players_tweets, os.path.join(team_dirpath, "two_players_tweets.tsv"))
    print_tweets_in_file(many_players_tweets, os.path.join(team_dirpath, "many_players_tweets.tsv"))


def print_tweets_in_file(tweets, tweets_fpath):

    with open(tweets_fpath, 'w') as no_player_file:
        for tweet in tweets:
            tweet.print_in_tsv_file(no_player_file)


def parse_dir_match(match_dirpath):

    # events = read_tsv_events_file("../../Data/events/event_types.tsv")

    fname_lst = [f for f in os.listdir(match_dirpath)
                 if not f.startswith('.')]  # Remove hidden files

    print(fname_lst)

    for fname in fname_lst:
        match_fpath = os.path.join(match_dirpath, fname)

        players = read_tsv_player_file("list_players.tsv", match_fpath)

        tweets = read_tsv_tweet_file(match_fpath, players)

        print_cluster_tweets(tweets, match_fpath)


if __name__ == "__main__":

    start_time = time.time()

    parse_dir_match('../../Data/match')

    print("--- %s seconds ---" % (time.time() - start_time))

    # for tweet in tweets :
    #    tweet.print_tweet()

    # players = [] #read_tsv_player_file(os.path.join("list_players"))

    # for player in players :
    #    player.print_player()
    #    teams.add(player.team)
