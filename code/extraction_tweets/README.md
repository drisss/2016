# Extraction

Global extractor: ./extract_all.sh path/to/the/folder

For every .json file in the provided path, creates an associated
.json.tsv file with the selected fields:
id time text retweet_count lang

# Grouping

Grouping tweets per event (N minutes span after the event): 
./tweets_per_event.sh N path/to/the/folder
