#!/bin/bash

HELP="Syntax: $0 N path/to/train_euro2016/

For every .json.tsv file in the provided path, creates an associated
folder containing files for tweets following events after N minutes.
Syntax of the files: the first line reports the event, the following
are the tweets retrieved."

if (( $# != 2 ))
then
  printf "%s\n" "$HELP" >&2
  exit
fi

path=$2
time_shift=$1

find $path -name "*.json.tsv" | while read file
do
  base_filename=$(echo $file | rev | cut -b 10- | rev)
  annotation_file=${base_filename}.tsv
  if ! test -f "$annotation_file"
  then
    printf "No file named %s\n" "$annotation_file" >&2
  else
    printf "Directory %s\n" "$base_filename"
    mkdir -p ${base_filename}_per_event
    ./tweets_per_event.lua $time_shift $annotation_file < $file
    if (( $? != 0 ))
    then
      exit 1
    fi
  fi
done

