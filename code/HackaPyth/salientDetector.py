__author__ = 'driss'
import os
from Tweet import Tweet
from Player import Player
from TSVreader import read_tsv_player_file, read_tsv_tweet_file
from collections import defaultdict
import collections
import datetime
import heapq
import matplotlib.pyplot as plt
import sys

tweets_with_no_player = []
tweets_with_a_team_no_player = []
tweets_with_single_players = []
tweets_with_two_players = []
tweets_with_many_players = []

filename = sys.argv[1]

tweets = read_tsv_tweet_file(os.path.join(filename))
events = defaultdict(str)
i = 0
for line in open('France_Roumanie_2016-06-10_21h_fr.tsv').readlines():
  i = i + 1
  line = line.replace('\n','')
  parts = line.split('\t')
  if i == 1:
    continue
  t = datetime.datetime.strptime(parts[0], "%H:%M:%S")
  t = t-datetime.timedelta(minutes=t.minute % 5,seconds=t.second)
  events[t]+="-"+line[9:].replace("\t"," ")
  

players = read_tsv_player_file(os.path.join("list_players"))
teams = set()
for player in players :
#    player.print_player()
    teams.add(player.team)


def cluster_tweets(tweets) :
    players_in_time = defaultdict(list)
    teams_in_time = defaultdict(list)
    all_dates = set()
    for tweet in tweets :
        nb_players,player_m = containPlayer(tweet)
        nb_teams,team_m = containTeam(tweet)
        if nb_players == 0 and nb_teams > 0 :
            tweets_with_a_team_no_player.append(tweet)
        elif nb_players == 0 :
            tweets_with_no_player.append(tweet)
        elif nb_players == 1 :
            tweets_with_single_players.append(tweet)
        elif nb_players == 2 :
            tweets_with_two_players.append(tweet)
        else :
            tweets_with_many_players.append(tweet)
        for t in team_m:
          teams_in_time[t[0]].append(tweet.date)
        for p in player_m:
          players_in_time[p[0]].append(tweet.date)
        all_dates.add(tweet.date)
#    print players_in_time.keys()[0]
    #print players_in_time[players_in_time.keys()[0]]
    mindate,maxdate,impdates = getinfodates(all_dates)
    graphintime(players_in_time,impdates)

def getinfodates(dates):
  tdates = [datetime.datetime.strptime(x, "%H:%M:%S") for x in dates]
  mindate = min(tdates)
  maxdate = max(tdates)
  impdates = set()
  for t in tdates:
      t = t-datetime.timedelta(minutes=t.minute % 5,seconds=t.second)
      impdates.add(t)
  return mindate,maxdate,sorted(list(impdates))
  
def splitbyteam(mentionsplayer):
  d1 = {}
  d2 = {}
  teams = list(set([x.team for x in mentionsplayer.keys()]))
#  print teams
  for key in mentionsplayer:
    if key.team == teams[0]:
      d1[key] = mentionsplayer[key]
    elif key.team == teams[1]:
      d2[key] = mentionsplayer[key]
#  print d1
#  print d2
  return d1,d2

def graphintime(d,xdates):
  do ={}
  total_mentions_by_player = {}
  for key in d:
#    print key.firstname
    myplayertime = defaultdict(float)
    for st in d[key]:
      t = datetime.datetime.strptime(st, "%H:%M:%S")
      t = t-datetime.timedelta(minutes=t.minute % 5,seconds=t.second)
      myplayertime[t]+=1.0
    for xd in xdates:
      if not xd in myplayertime:
        myplayertime[xd] = 0.0
    omyplayertime = collections.OrderedDict(sorted(myplayertime.items()))
    do[key]=omyplayertime
    total_mentions_by_player[key]=sum(omyplayertime.values())
  players_top_but = heapq.nlargest(5, total_mentions_by_player, key=total_mentions_by_player.get)
  labelidlist = [x+y for x in ['-o','-*','->','-.','-<','-','--',':','steps' ] for y in ['r','g','b','c','m','y']]
  fig = plt.figure(figsize=(25,12))
  ax = fig.add_subplot(111)
  i = 0
  allplayersmentions = {}
  for key in do:
    omyplayertime = do[key]
    ax.plot(omyplayertime.keys(),omyplayertime.values(),labelidlist[i%50],label=key.firstname.decode('unicode-escape')+" "+key.lastname.decode('unicode-escape'))
    i = i + 1
    if key in players_top_but:
       top_but = heapq.nlargest(1, omyplayertime, key=omyplayertime.get)
       print str(top_but)[31:33]+":"+str(top_but)[35:37]+":00\t"+key.lastname+"\tBUT"
     
  for key in events:
    ax.annotate(events[key], xy=(key, 50),rotation=-15, xytext=(key, -200),arrowprops=dict(facecolor='black', shrink=0.05))
  ax.set_xlabel("Time", fontsize=10)
  ax.set_ylabel("Freq", fontsize=10)
  ax.legend(loc="best")
  ax.margins(0.1)
  fig.tight_layout()
  plt.savefig("france_roumanie.png")    
  fig = plt.figure(figsize=(25,12))
  ax = fig.add_subplot(111)
  total_mentions_by_player_team1, total_mentions_by_player_team2 = splitbyteam(total_mentions_by_player)
  players_top_k_team1 = heapq.nlargest(5, total_mentions_by_player_team1, key=total_mentions_by_player_team1.get)
  players_top_k_team2 = heapq.nlargest(5, total_mentions_by_player_team2, key=total_mentions_by_player_team2.get)
  players_top_k = players_top_k_team1 + players_top_k_team2
  i = 0
  for key in do:
    omyplayertime = do[key]
    if not key in players_top_k:
      continue
    values = [x/total_mentions_by_player[key] for x in do[key].values()]
    ax.plot(omyplayertime.keys(),values,labelidlist[i],label=key.firstname.decode('unicode-escape')+" "+key.lastname.decode('unicode-escape')+" "+key.team,linewidth=1.0)
    i = i + 1
    picks = {}
    postneg = 1
    last = omyplayertime[omyplayertime.keys()[0]]
    lastkey = omyplayertime.keys()[0]
    for xkey in omyplayertime:
      xval = omyplayertime[xkey]
      if last > xval:
        if postneg == -1:
          picks[lastkey] = omyplayertime[lastkey]
        postneg = 1
      else:
        postneg = -1
      last = xval
      lastkey = xkey
    top_picks = heapq.nlargest(min(3,len(picks)), picks, key=picks.get)
    for x in picks:
      if x in top_picks:
        print str(x)[11:]+"\t"+key.lastname+"\tTIR"
#  print events
  for key in events:
    ax.annotate(events[key], xy=(key, 0.0),rotation=-15, xytext=(key, -0.03),arrowprops=dict(facecolor='black', shrink=0.05))
  ax.set_xlabel("Time", fontsize=10)
  ax.set_ylabel("Freq", fontsize=10)
  ax.legend(loc="best")
  ax.margins(0.1)
  fig.tight_layout()
  plt.savefig("france_roumanie_normalized.png")    
def containPlayer(tweet) :
    text = tweet.getText()
    nb_players = 0
    player_mention = []
    for player in players :
        if not (player.team == "france" or player.team == "roumanie"):
            continue

#        if (player.getFirstName() in text.lower()) or (player.getLastName() in text.lower()) :
        if  (player.getLastName() in text.lower()) :
            nb_players = nb_players + 1
            player_mention.append((player,tweet))
    return nb_players,player_mention

def containTeam(tweet) :
    text = tweet.getText()
    nb_teams = 0
    team_mention = []
    for team in teams :
        if (team in text.lower()) or (team in text.lower()) :
            nb_teams = nb_teams + 1
            team_mention.append((team,tweet))
    return nb_teams,team_mention

cluster_tweets(tweets)

##print("tweets_with_a_team_no_player:", tweets_with_a_team_no_player.__len__())
##print("tweets_with_no_player :",tweets_with_no_player.__len__())
##print("tweets_with_single_players: ", tweets_with_single_players.__len__())
##print("tweets_with_two_players:",tweets_with_two_players.__len__())
##print("tweets_with_many_players:", tweets_with_many_players.__len__())
