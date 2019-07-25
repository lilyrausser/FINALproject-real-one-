import pygame
import random 
import time
import pygame.freetype
from constants import *

class ColorBox(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        # self.input = input_dict
        self.selected = False
        self.color = color

        self.images = {}

        self.set_color(color)
        self.set_selected(self.selected)

        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (189, 189))

        self.set_position()

        self.timer = 0
        self.time_limit = 15
        self.activated = False


    def set_position(self):
        if self.color == RED:
            self.rect.x = 404
            self.rect.y = 146
        elif self.color == GREEN: 
            self.rect.x = 215
            self.rect.y = 146
        elif self.color == YELLOW:
            self.rect.x = 404
            self.rect.y = 335
        elif self.color == BLUE:
            self.rect.x = 215
            self.rect.y = 335
        

    #def clicked(self):



    def set_color(self, color):
        if color == RED:
            self.images["Bright"] = pygame.image.load("assets/images/red_bright.png")
            self.images["Dull"] = pygame.image.load("assets/images/red_dull.png")
        elif color == GREEN:
            self.images["Bright"] = pygame.image.load("assets/images/green_bright.png")
            self.images["Dull"] = pygame.image.load("assets/images/green_dull.png")
        elif color == BLUE:
            self.images["Bright"] = pygame.image.load("assets/images/blue_bright.png")
            self.images["Dull"] = pygame.image.load("assets/images/blue_dull.png")
        elif color == YELLOW:
            self.images["Bright"] = pygame.image.load("assets/images/yellow_bright.png")
            self.images["Dull"] = pygame.image.load("assets/images/yellow_dull.png")

        self.images["Bright"] = pygame.transform.scale(self.images["Bright"], (189, 189))
        self.images["Dull"] = pygame.transform.scale(self.images["Dull"], (189, 189))


    def set_selected(self, selected):
        if selected:
            self.image = self.images["Bright"]
        else:
            self.image = self.images["Dull"]
        
    def activate(self):
        self.activated = True
        self.image = self.images["Bright"]

    def update(self):  
        if self.activated:
            self.timer += 1
            if self.timer >= self.time_limit:
                self.activated = False
                self.image = self.images["Dull"]
                self.timer = 0