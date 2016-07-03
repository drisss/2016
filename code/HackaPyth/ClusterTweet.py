__author__ = 'driss'
import os
from Tweet import Tweet
from Player import Player
from TSVreader import read_tsv_player_file, read_tsv_tweet_file


def cluster_tweets(tweets, players, teams) :
    for tweet in tweets :
        if len(tweet.players) == 0 :
            if (len(tweet.teams) == 1) :
                tweets_with_a_team_no_player.append(tweet)
            else :
                tweets_with_no_player.append(tweet)

        elif len(tweet.players) == 1 :
            tweets_with_single_players.append(tweet)
        elif len(tweet.players) ==  2 :
            tweets_with_two_players.append(tweet)
        else :
            tweets_with_many_players.append(tweet)


def containPlayer( text, players) :
    nb_players = 0
    for player in players :

        if (player.getFirstName() in text.lower()) or (player.getLastName() in text.lower()) :
            nb_players = nb_players + 1
    return nb_players

def containTeam(text,teams) :
    nb_teams = 0
    for team in teams :

        if (team in text.lower()) or (team in text.lower()) :
            nb_teams = nb_teams + 1
    return nb_teams



if __name__ == "__main__":

    tweets_with_no_player = []
    tweets_with_a_team_no_player = []
    tweets_with_single_players = []
    tweets_with_two_players = []
    tweets_with_many_players = []


    tweets = read_tsv_tweet_file(os.path.join("France_Roumanie_2016-06-10_21h_fr.json.tsv"), "list_players")

    #for tweet in tweets :
    #    tweet.print_tweet()

    #players = [] #read_tsv_player_file(os.path.join("list_players"))


    #for player in players :
    #    player.print_player()
    #    teams.add(player.team)



    cluster_tweets(tweets,players,teams)

    print("tweets_with_a_team_no_player:", len(tweets_with_a_team_no_player))
    print("tweets_with_no_player :",len(tweets_with_no_player.__len__()))
    print("tweets_with_single_players: ", len(tweets_with_single_players.__len__()))
    print("tweets_with_two_players:",len(tweets_with_two_players.__len__()))
    print("tweets_with_many_players:", len(tweets_with_many_players.__len__()))