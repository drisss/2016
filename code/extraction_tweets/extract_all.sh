#!/bin/bash

HELP="Syntax: $0 path/to/train_euro2016/

For every .json file in the provided path, creates an associated
.json.tsv file with the selected fields:
id time text retweet_count lang"

if (( $# == 0 ))
then
  printf "%s\n" "$HELP" >&2
  exit
fi

path=$1

find $path -name "*.json" | while read file
do
  printf "%s -> " "$file" >&2
  ( ./parse_json_line.lua < $file > ${file}.tsv && printf "%s\n" "${file}.tsv" >&2)
  if (( $? != 0 ))
  then
    printf "error\n" >&2
    exit 1
  fi
done
