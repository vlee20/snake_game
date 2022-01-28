#!/usr/bin/env python3
# Vincent Lee
# CPSC 386-01
# 2021-11-29
# lee.v3798@csu.fullerton.edu
# @vlee20
#
# Lab 04-00
#
# This program is the main file so the game can run and stop
#

"""This module is the main file to run the game"""

from snake_game import SnakeGame


def main():
    """This main starts the loop for the game to start"""
    return SnakeGame().run()


if __name__ == "__main__":
    main()
