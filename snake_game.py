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

"""This module is for the Snake Game class"""

from snake_obj import Snake
from fruit import Fruit
from player import Player
import scene
import pygame

FIREBRICK = (178, 34, 34)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PEACH = (255, 218, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCENE_TITLE = 0
SCENE_INSTRUCT = 1
SCENE_GAME = 2
SCENE_OVER = 3
END = 4
EXIT = 5

CELLSIZE = 20
WINDOWSIZE = (800, 800)
CELLWIDTH = int(WINDOWSIZE[0] / CELLSIZE)
CELLHEIGHT = int(WINDOWSIZE[1] / CELLSIZE)

TITLEM_DIR = "music/Blasterhead_-_01_-_Skyblue_Monday-[AudioTrimmer.com].mp3"
GAMEM_DIR = "music/Blasterhead_-_03_-_HARAKIRI_NATION-[AudioTrimmer.com].mp3"


def display_info():
    """Print out information about the display driver and video information"""
    print(
        "The display is using the '{}' driver".format(
            pygame.display.get_driver()
        )
    )
    print("Video Info:")
    print(pygame.display.Info())


class SnakeGame:

    """This is the Snake Game class"""

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.player = Player()

    def restart(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.player = Player()

    def run(self):
        """This is the entry point to the game. It is the main function"""

        if not pygame.font:
            print("Warning: fonts disabled.")

        if not pygame.mixer:
            print("Warning: sound disabled.")

        # allows libraries to initialize to work together
        pygame.init()
        display_info()
        screen = pygame.display.set_mode(WINDOWSIZE)
        title = "SHNAKEE"
        pygame.display.set_caption(title)
        start = True
        scene_num = SCENE_TITLE
        pygame.mixer.music.load(TITLEM_DIR)
        pygame.mixer.music.set_volume(0.08)
        pygame.mixer.music.play(-1)
        while start:
            if scene_num == SCENE_TITLE:
                title_scene = scene.TitleScene(
                    screen, RED, "Shnakiez", BLACK, 36
                )
                scene_game = title_scene
                scene_game.start()
                scene_num = scene_game.process_event()
            elif scene_num == SCENE_INSTRUCT:
                instruction_scene = scene.InstructionScene(
                    screen, BLUE, WHITE, 18
                )
                scene_game = instruction_scene
                scene_num = scene_game.process_event()
            elif scene_num == SCENE_GAME:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(GAMEM_DIR)
                pygame.mixer.music.set_volume(0.02)
                pygame.mixer.music.play(-1)
                self.restart()
                game_scene = scene.GameScene(screen, PEACH, self.player)
                scene_game = game_scene
                scene_num = scene_game.process_event()
            elif scene_num == SCENE_OVER:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(TITLEM_DIR)
                pygame.mixer.music.set_volume(0.08)
                pygame.mixer.music.play(-1)
                self.player.score_file()
                over_scene = scene.GameOver(screen, FIREBRICK, self.player, 36)
                scene_game = over_scene
                scene_num = scene_game.process_event()
                if scene_num == END:
                    scene_game.end()
                    start = False
            elif scene_num == EXIT:
                break

        print("Exiting!")
        pygame.quit()

        return 0
