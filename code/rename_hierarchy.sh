#!/bin/bash

HELP="Syntax: $0 path/to/train_euro2016/"

if (( $# != 1 ))
then
  printf "%s\n" "$HELP" >&2
  exit
fi

path=$1

find $path -type f | while read file
do
  mv -v $file $(echo "$file" | iconv -f utf8 -t ascii//TRANSLIT)
done
