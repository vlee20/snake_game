# Vincent Lee
# CPSC 386-01
# 2021-11-29
# lee.v3798@csu.fullerton.edu
# @vlee20
#
# Lab 04-00
#
# This program has the functions/objects (classes) of the snake game and how it operates
#

"""This module is for the Player class"""

from datetime import date
import json


class Player:

    """This is the Player class"""

    def __init__(self):
        self.points = 1
        self.time = 0
        today = date.today()
        date_string = today.strftime("%m/%d/%Y")
        self.date = date_string

    def format_json(self):
        """formats to json file"""
        data = {"Score": self.points, "Time": self.time, "Date": self.date}
        return data

    def score_file(self):
        """writes to a file"""
        with open("leaderboard.txt", "a") as score_file:
            json.dump(self.format_json(), score_file)
            score_file.write("\n")
