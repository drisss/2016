#!/bin/bash

input_file=$1
team1=$(echo $input_file | cut -f 1 -d "_")
team2=$(echo $input_file | cut -f 2 -d "_")
date=$(echo $input_file | cut -f 3 -d "_")

json_tsv=$(mktemp)

pushd extraction_tweets
./parse_json_line.lua < $input_file > $json_lua
popd

# filtres Anne-Lise

tmp=$(mktemp)

python HackaPyth/salientDetector.py < $json_tsv | sort > $tmp

tmp_time=$(mktemp)
tmp_arg=$(mktemp)
tmp_evt=$(mktemp)

cut -f 1 < $tmp > $tmp_time
cut -f 2 < $tmp > $tmp_arg
cut -f 3 < $tmp > $tmp_evt

paste $tmp_time $tmp_evt $tmp_arg

# post treatment (?)



rm -f $tmp $tmp_time $tmp_arg $tmp_evt
