import pygame
import random 
import time
import pygame.freetype
from constants import RED, YELLOW, BLUE, GREEN, FPS, WIDTH, HEIGHT, DISPLAY, PLAY, FAILED, START, PLAY_BUTTON, BACK_BUTTON, QUIT_BUTTON, REPLAY_BUTTON, RULES_BUTTON

class Backdrop(pygame.sprite.Sprite):
    """The backdrop image for the game"""
    def __init__(self, backdrop_type):
        super().__init__()

        self.images  =  {}
        self.images["game_page"] = pygame.image.load("assets/backgrounds/start_page.jpg")
        self.images["failed_page"] = pygame.image.load("assets/backgrounds/you_lost.jpg")
        self.images["rules"] =  pygame.image.load("assets/backgrounds/rules.jpg")
        self.images["start_game"] = pygame.image.load("assets/backgrounds/start_page.jpg")
        self.images["quit"] = pygame.image.load("assets/backgrounds/quit_page.jpg")
        
        self.image = self.images[backdrop_type]

        self.rect = self.image.get_rect()
        self.rect.w


                

                               



                            
                                


                                


