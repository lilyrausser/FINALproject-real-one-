import pygame
import random 
import time
import pygame.freetype
from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, button_type):
        super().__init__()
        self.images = {}
        self.images[EASY_BUTTON] = pygame.image.load("assets/sprites/easy_level.png")
        self.images[HARD_BUTTON] = pygame.image.load("assets/sprites/hard_level.png")
        self.images[BACK_BUTTON] = pygame.image.load("assets/sprites/back_button.png")
        self.images[QUIT_BUTTON] = pygame.image.load("assets/sprites/quit_button.png")
        self.images[REPLAY_BUTTON] = pygame.image.load("assets/sprites/replay_button.png")
        self.images[RULES_BUTTON] = pygame.image.load("assets/sprites/rules_button.png")

        self.set_type(button_type)


    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        
        
    def set_type(self, button_type):
        self.button_type = button_type
        self.image = self.images[button_type]    

        self.rect = self.image.get_rect()
        
