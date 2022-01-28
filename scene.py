# Vincent Lee
# CPSC 386-01
# 2021-11-29
# lee.v3798@csu.fullerton.edu
# @vlee20
#
# Lab 04-00
#
# This program has the Scenes that makes the flow of the game and is able to draw it
#

"""This module is able to draw on the screen and interact with the user to play the game"""

from datetime import date
from fruit import Fruit
from snake_obj import Snake
import pygame

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

WHITE = (255, 255, 255)

SCENE_TITLE = 0
SCENE_INSTRUCT = 1
SCENE_GAME = 2
SCENE_OVER = 3
END = 4
EXIT = 5
CLOCK = pygame.time.Clock()
CELLSIZE = 20

EATSOUND_DIR = "music/Recording (10)-[AudioTrimmer.com] (1).wav"
DEATHSOUND_DIR = "music/deathsound.wav"


class Scene:

    """This is the Scene class"""

    def __init__(self, screen, background_color):
        self._is_valid = True
        self._frame_rate = 15
        self._screen = screen
        # Everything is a surface, fits in a rectangle
        self._background = pygame.Surface(self._screen.get_size())
        self._background_color = background_color
        self._background.fill(self._background_color)

    def is_valid(self):
        """This checks if the screen is valid to move to the other screen"""
        return self._is_valid

    def frame_rate(self):
        """Saves the framerate of the scene"""
        return self._frame_rate

    def start(self):
        """When the game starts"""
        print("game starting...")

    def end(self):
        """When the game is ending"""
        print("game ending")

    def update(self):
        """When the game updates"""
        pass

    # draw to a screen with color
    def draw(self):
        """Draws onto the screen for the user"""
        # draw onto a screen with color
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Where inputs are being captured"""
        for event_key in pygame.event.get():
            if event_key.type == pygame.QUIT:
                print("Good Bye!")
                self._is_valid = False
            if (event_key.type == pygame.KEYDOWN) and (
                event_key.type == pygame.K_ESCAPE
            ):
                print("Bye bye!")
                self._is_valid = False


class TitleScene(Scene):

    """This is the Title Scene class"""

    def __init__(
        self, screen, background_color, title, title_color, title_size
    ):
        super().__init__(screen, background_color)
        # print('Hi there is a titlescreen')
        self._title_color = title_color
        self._title_size = title_size
        title_font = pygame.font.Font(
            pygame.font.get_default_font(), title_size
        )
        info = "Press any key to continue"
        info_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        # return a surface where it is applied, need to figure where to apply it
        self._title = title_font.render(title, True, title_color)
        self._cont = info_font.render(info, True, title_color)
        (width, height) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(width / 2, height / 2))
        self._info_pos = self._cont.get_rect(center=(width / 2, height / 1.25))

    def process_event(self):
        """Where inputs are being captured in the Title Screen"""
        while self._is_valid:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._is_valid = False
                    return SCENE_INSTRUCT
                if event.type == pygame.QUIT:
                    return EXIT
            self.update()
            self.draw()
            pygame.display.update()

    def draw(self):
        """Where it is being drawn in the Title Scene"""
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._cont, self._info_pos)


class InstructionScene(Scene):

    """This is the Instruction Scene"""

    def __init__(self, screen, background_color, title_color, title_size):
        super().__init__(screen, background_color)
        self._title_color = title_color
        self._title_size = title_size
        title_font = pygame.font.Font(
            pygame.font.get_default_font(), title_size
        )
        title = "Try to eat as many as you can without touching the walls or eating yourself!"
        upward = "Up Arrow Key goes up"
        left = "Left Arrow Key goes left"
        right = "Right Arrow Key goes right"
        down = "Down Arrow Key goes down"
        enter = "Press Enter to start!"
        # return a surface where it is applied, need to figure where to apply it
        self._title = title_font.render(title, True, title_color)
        self._up = title_font.render(upward, True, title_color)
        self._left = title_font.render(left, True, title_color)
        self._right = title_font.render(right, True, title_color)
        self._down = title_font.render(down, True, title_color)
        self._enter = title_font.render(enter, True, title_color)
        (width, height) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(width / 2, height / 6))
        self._up_pos = self._up.get_rect(center=(width / 2, height / 4))
        self._left_pos = self._left.get_rect(center=(width / 2, height / 3.60))
        self._right_pos = self._right.get_rect(
            center=(width / 2, height / 3.25)
        )
        self._down_pos = self._down.get_rect(center=(width / 2, height / 3))
        self._enter_pos = self._enter.get_rect(
            center=(width / 2, height / 1.25)
        )

    def process_event(self):
        """This captures the inputs in the Instruction Scene"""
        while self._is_valid:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN) and (
                    event.key == pygame.K_RETURN
                ):
                    self._is_valid = False
                    return SCENE_GAME
                if event.type == pygame.QUIT:
                    return EXIT
            self.update()
            self.draw()
            pygame.display.update()

    def draw(self):
        """Drawn in the Instruction Scene"""
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._up, self._up_pos)
        self._screen.blit(self._left, self._left_pos)
        self._screen.blit(self._right, self._right_pos)
        self._screen.blit(self._down, self._down_pos)
        self._screen.blit(self._enter, self._enter_pos)


class GameScene(Scene):

    """This is the Game Scene"""

    def __init__(self, screen, background_color, player):
        super().__init__(screen, background_color)
        self.snake = Snake()
        self.fruit = Fruit()
        self._screen = screen
        self.gamer = player
        self.score = player.points
        self.time = player.time
        self.date = date.today()
        self.exit = False
        self.eat_sound = pygame.mixer.Sound(EATSOUND_DIR)
        self.death_sound = pygame.mixer.Sound(DEATHSOUND_DIR)

    def process_event(self):
        """This captures the inputs in the Game Scene and is able to update and draw"""
        # the timer
        time_delay = 1000
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, time_delay)
        while self._is_valid:
            CLOCK.tick(self._frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return EXIT
                self.snake.control(event)
                if event.type == timer_event:
                    self.time += 1
                    self.gamer.time += 1
                    if self.gamer.time % 3 == 0 and self.gamer.time != 0:
                        self.gamer.points += 1
            self.update()
            self.draw()
            pygame.display.update()
            if self.exit:
                break
        if self.exit:
            return SCENE_OVER

    def update(self):
        """Updates the worm so it can move visually"""
        self.snake.update()
        eaten = self.fruit.b_collision(
            self.snake.worm_body[0]["x"] * CELLSIZE,
            self.snake.worm_body[0]["y"] * CELLSIZE,
        )
        if eaten == True:
            self.eat_sound.play()
            self.snake.eat()
            self.snake.length += 1
            self.score += 1
            self.gamer.points += 1
            self._frame_rate += 1
        self._is_valid = self.snake.b_collision()
        if self._is_valid == False:
            self.death_sound.play()
            self.exit = True
        self._is_valid = self.snake.check_duplicate()
        if self._is_valid == False:
            self.death_sound.play()
            self.exit = True

    def display_score(self, points):
        """Displays the score on the top right"""
        score_font = pygame.font.Font(pygame.font.get_default_font(), 25)
        score = score_font.render(f"Score: {points}", True, (255, 255, 255))
        score_pos = score.get_rect(topleft=(680, 100))
        self._screen.blit(score, score_pos)

    def draw(self):
        """Drawn on the screen in the Game Scene class"""
        super().draw()
        self.fruit.draw(self._screen)
        self.snake.draw(self._screen)
        self.display_score(self.gamer.points)


class GameOver(Scene):

    """This is the Game Over class"""

    def __init__(self, screen, background_color, player, title_size):
        super().__init__(screen, background_color)
        self.gamer = player
        over_font = pygame.font.Font(pygame.font.get_default_font(), 75)
        message_font = pygame.font.Font(
            pygame.font.get_default_font(), title_size
        )
        stat_font = pygame.font.Font(pygame.font.get_default_font(), 40)
        stat = f"Score: {self.gamer.points}  Time: {self.gamer.time}s  Date: {self.gamer.date}"
        message = "Game Over!"
        restart_message = "Press R to restart"
        escape_message = "Press ESC to quit"
        self._message = over_font.render(message, True, WHITE)
        self._restart_message = message_font.render(
            restart_message, True, WHITE
        )
        self._escape_message = message_font.render(escape_message, True, WHITE)
        self._stat = stat_font.render(stat, True, WHITE)
        (width, height) = self._screen.get_size()
        self._message_pos = self._message.get_rect(
            center=(width / 2, height / 2)
        )
        self._restart_pos = self._restart_message.get_rect(topleft=(50, 600))
        self._escape_pos = self._escape_message.get_rect(topleft=(450, 600))
        self._stat_pos = self._stat.get_rect(topleft=(50, 100))

    def process_event(self):
        """Captures the inputs in the Game Over classs"""
        while self._is_valid:
            for event in pygame.event.get():
                # super().process_event()
                if event.type == pygame.KEYUP and event.key == pygame.K_r:
                    self._is_valid = False
                    return SCENE_INSTRUCT
                if event.type == pygame.QUIT:
                    self._is_valid = False
                    return EXIT
                if (event.type == pygame.KEYDOWN) and (
                    event.key == pygame.K_ESCAPE
                ):
                    self._is_valid = False
                    return END
            self.update()
            self.draw()
            pygame.display.update()

    def draw(self):
        """Drawn onto the screen for the Game Over scene"""
        super().draw()
        self._screen.blit(self._message, self._message_pos)
        self._screen.blit(self._restart_message, self._restart_pos)
        self._screen.blit(self._escape_message, self._escape_pos)
        self._screen.blit(self._stat, self._stat_pos)
