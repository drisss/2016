import os
from Tweet import Tweet
from Player import Player
from TSVreader import read_tsv_player_file, read_tsv_tweet_file
import time

__author__ = 'driss'


clustered_tweets_dir = "../../Data/clustered_tweets/"


def print_cluster_tweets(tweets, match_fpath):

    match_fname = os.path.basename(match_fpath)
    match_basename = os.path.splitext(match_fname)[0]
    team_names = match_basename.lower().split('_')[:2]

    dir_team = team_names[0] + '_' + team_names[1]
    team_dirpath = os.path.join(clustered_tweets_dir, dir_team)

    if not os.path.exists(team_dirpath):
        os.makedirs(team_dirpath)

    tweets_with_no_player = []
    tweets_with_a_team_no_player = []
    tweets_with_single_players = []
    tweets_with_two_players = []
    tweets_with_many_players = []

    for tweet in tweets:
        if len(tweet.players) == 0:
            if len(tweet.teams) == 1:
                tweets_with_a_team_no_player.append(tweet)
            else:
                tweets_with_no_player.append(tweet)

        elif len(tweet.players) == 1:
            tweets_with_single_players.append(tweet)
        elif len(tweet.players) == 2:
            tweets_with_two_players.append(tweet)
        else:
            tweets_with_many_players.append(tweet)

    print("tweets_with_a_team_no_player:", len(tweets_with_a_team_no_player))
    print("tweets_with_no_player :", len(tweets_with_no_player))
    print("tweets_with_single_players: ", len(tweets_with_single_players))
    print("tweets_with_two_players:", len(tweets_with_two_players))
    print("tweets_with_many_players:", len(tweets_with_many_players))

    print_tweets_in_file(tweets_with_no_player, os.path.join(team_dirpath, "tweets_with_no_player.tsv"))
    print_tweets_in_file(tweets_with_a_team_no_player, os.path.join(team_dirpath,"tweets_with_a_team_no_player.tsv"))
    print_tweets_in_file(tweets_with_single_players, os.path.join(team_dirpath,"tweets_with_single_players.tsv"))
    print_tweets_in_file(tweets_with_two_players, os.path.join(team_dirpath,"tweets_with_two_players.tsv"))
    print_tweets_in_file(tweets_with_many_players, os.path.join(team_dirpath,"tweets_with_many_players.tsv"))



def contain_event(tweet, events):
    


def print_tweets_in_file(tweets, tweets_fpath):

    with open(tweets_fpath, 'w') as no_player_file:
        for tweet in tweets:
            tweet.print_in_tsv_file(no_player_file)


def parse_dir_match(match_dirpath):
    fname_lst = [f for f in os.listdir(match_dirpath)]

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


