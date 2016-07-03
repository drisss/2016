#!/bin/env python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Usage:  python3 ~/scripts_tat/run_lf0_max_from_numpy.py show
#   From:   /Users/mev/Dropbox/SHARE_UBUNTU/lf0/lf0
#

import datetime

class tweet:

    """Classe définissant un tweet caractérisée par :
    son text """


    def __init__(self, date, text,nb_retweet): # Notre méthode constructeur

        self.date = date
        self.text = text
        self.nb_retweet = nb_retweet


    def print_tweet(self):
        print(self.date,self.text)
