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

"""This module is for the Snake object class"""

import random
import pygame

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

CELLSIZE = 20
WINDOWSIZE = (800, 800)
CELLWIDTH = int(WINDOWSIZE[0] / CELLSIZE)
CELLHEIGHT = int(WINDOWSIZE[1] / CELLSIZE)


class Snake:

    """This is the Snake class"""

    def __init__(self):
        self.startx = random.randint(5, CELLWIDTH - 6)
        self.starty = random.randint(5, CELLHEIGHT - 6)
        self.x_change = 0
        self.y_change = 0
        self.worm_body = [
            {"x": self.startx, "y": self.starty},
            {"x": self.startx - 1, "y": self.starty},
            {"x": self.startx - 2, "y": self.starty},
        ]
        self.direction = ""
        self.length = len(self.worm_body)

    def control(self, event):
        """controls the snake"""
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) and self.direction != RIGHT:
                self.x_change = -1
                self.y_change = 0
                self.direction = LEFT
            elif (event.key == pygame.K_RIGHT) and self.direction != LEFT:
                self.x_change = 1
                self.y_change = 0
                self.direction = RIGHT
            elif (event.key == pygame.K_DOWN) and self.direction != UP:
                self.y_change = 1
                self.x_change = 0
                self.direction = DOWN
            elif (event.key == pygame.K_UP) and self.direction != DOWN:
                self.y_change = -1
                self.x_change = 0
                self.direction = UP

    def update(self):
        """Updates the worm so it can move visually"""
        self.worm_body[0]["x"] += self.x_change
        self.worm_body[0]["y"] += self.y_change
        # print(self.worm_body[0])

        for i in range(self.length - 1, 0, -1):
            self.worm_body[i]["x"] = self.worm_body[i - 1]["x"]
            self.worm_body[i]["y"] = self.worm_body[i - 1]["y"]

    def eat(self):
        """when the snake eats the apple"""
        self.worm_body.append(
            {"x": self.worm_body[0]["x"], "y": self.worm_body[0]["y"]}
        )

    def b_collision(self):
        """when the snake collides with the boarder"""
        alive = True
        full_x = self.worm_body[0]["x"] * CELLSIZE
        full_y = self.worm_body[0]["y"] * CELLSIZE
        if full_x >= 800 or full_x < 0 or full_y >= 800 or full_y < 0:
            alive = False
        return alive

    def check_duplicate(self):
        """checks if there are an duplicates in the worm meaning it has collided"""
        worm_head = {"x": self.worm_body[2]["x"], "y": self.worm_body[2]["y"]}
        for coord in self.worm_body[3:]:
            if worm_head == coord:
                return False
        return True

    def draw(self, screen):
        """draws the snake"""
        for coord in self.worm_body:
            x_coord = coord["x"]
            y_coord = coord["y"]

            full_x = x_coord * CELLSIZE
            full_y = y_coord * CELLSIZE

            self.worm_rect = pygame.Rect(full_x, full_y, CELLSIZE, CELLSIZE)

            pygame.draw.rect(screen, (0, 155, 0), self.worm_rect)
