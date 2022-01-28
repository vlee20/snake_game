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

"""This module is for the Fruit class"""

import random
import pygame

CELLSIZE = 20
WINDOWSIZE = (800, 800)
CELLWIDTH = int(WINDOWSIZE[0] / CELLSIZE)
CELLHEIGHT = int(WINDOWSIZE[1] / CELLSIZE)


class Fruit:

    """This is the Fruit class"""

    def __init__(self):
        self.fruitx = random.randint(5, CELLWIDTH - 6)
        self.fruity = random.randint(5, CELLHEIGHT - 6)
        self.fruit_body = [{"x": self.fruitx, "y": self.fruity}]
        self.collided = False

    def update(self):
        """Updates the fruit"""
        self.fruit_body[0]["x"] = random.randint(5, CELLWIDTH - 6)
        self.fruit_body[0]["y"] = random.randint(5, CELLHEIGHT - 6)

    def b_collision(self, full_x, full_y):
        """when the snake collides with the fruit"""
        ate = False
        appx = self.fruit_body[0]["x"]
        appy = self.fruit_body[0]["y"]
        appx = appx * CELLSIZE
        appy = appy * CELLSIZE
        if (appx == full_x) and (appy == full_y):
            print("yum")
            ate = True
            self.update()
        return ate

    def draw(self, screen):
        """draws the fruit"""
        self.fruit = pygame.Rect(
            self.fruit_body[0]["x"] * CELLSIZE,
            self.fruit_body[0]["y"] * CELLSIZE,
            CELLSIZE,
            CELLSIZE,
        )
        pygame.draw.rect(screen, (255, 0, 0), self.fruit)
