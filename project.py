import pygame
import random 
import time
from constants import RED, YELLOW, BLUE, GREEN, FPS, WIDTH, HEIGHT


class Backdrop(pygame.sprite.Sprite):
    """The backdrop image for the game"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/backgrounds/start_page.jpg")

        self.rect = self.image.get_rect()
        self.rect.w

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
                
class Game():
    """A class that holds the entire game"""
    # pythons way of stating that something is being done to a specific object is called "self"
    def __init__(self):
        pygame.init()

        self.timer = 0
        self.time_limit = 80
        self.color_index = 0
        self.color_list = self.get_color_list(4)

        print(self.color_list)

        self.red_box = ColorBox(RED)
        self.yellow_box = ColorBox(YELLOW)
        self.blue_box = ColorBox(BLUE)
        self.green_box = ColorBox(GREEN)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True
        self.displaying_color = True
        self.backdrop = Backdrop()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.backdrop)
        self.sprites.add(self.green_box)
        self.sprites.add(self.yellow_box)
        self.sprites.add(self.blue_box)
        self.sprites.add(self.red_box)

        # self.self_squares = SelfSquares(self.sprites, self.input)

    def get_color_list(self, squares_per_level):
        """returns random list of colors"""
        color_options = [RED, YELLOW, BLUE, GREEN]
        color_list = []
        while len(color_list) < squares_per_level:
            color = random.choice(color_options)
            color_list.append(color)
        return color_list

    def display_color_list(self):
        if self.displaying_color == True: 
            self.timer += 1

            if self.timer == self.time_limit:
                self.timer = 0
                color = self.color_list[self.color_index]
                self.color_index += 1

                if color == RED:
                    self.red_box.activate()
                    print(color)

                elif color == GREEN:
                    self.green_box.activate()
                    print(color)

                elif color == YELLOW:
                    self.yellow_box.activate()
                    print(color)

                elif color == BLUE: 
                    self.blue_box.activate()
                    print(color)


                if self.color_index == len(self.color_list):
                    self.displaying_color = False
            


    def update(self):
        """Updates the game"""
        self.clock.tick(FPS)

        if self.phase == DISPLAY:
            self.display_color_list()
        elif self.phase == PLAY:
            game()

        # does all of the inputs and understands them
        
        self.handle_input()
        self.sprites.update()
        self.sprites.draw(self.screen)

        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for sprite in self.sprites:
                    if sprite.rect.collidepoint(pos):
                        list.append(sprite.color)
    
    maxfails = False
    fails = 0


    #storing data 
    #input(color)
    #with open("color_string.data.json", "w", encoding="utf-8") as outfile: 
    #json.dump(color_string_results, outfile, ensure_ascii=False, indent=2)

#with open("color_string_data.json") as infile: 
    #data = json.load(infile)

    #print(data)


    def score(self): 
        if maxfails = True:
            break #you lost interface
        else:
            game()











        
    
def main():
    game = Game()

    while game.running:
        game.update()

if __name__ == '__main__':
    main()
