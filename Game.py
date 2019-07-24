import pygame
import random 
import time
from Buttons import Button
from ColorBox import ColorBox
from Backdrop import Backdrop
from constants import RED, YELLOW, BLUE, GREEN, FPS, WIDTH, HEIGHT, DISPLAY, PLAY, FAILED, RULES, START, PLAY_BUTTON, BACK_BUTTON, QUIT_BUTTON, REPLAY_BUTTON, RULES_BUTTON, QUIT

class Game():
    """A class that holds the entire game"""
    # pythons way of stating that something is being done to a specific object is called "self"
    def __init__(self):
        pygame.init()


        self.phase = START
        self.current_index = 0
        self.timer = 0
        self.time_limit = 40
        self.color_index = 0
        self.total_colors = 4
        self.total_score  = 0
        self.color_list = self.get_color_list(self.total_colors)

        self.red_box = ColorBox(RED)
        self.yellow_box = ColorBox(YELLOW)
        self.blue_box = ColorBox(BLUE)
        self.green_box = ColorBox(GREEN)

        self.play_button = Button(PLAY_BUTTON)
        self.play_button.set_pos(350,250)
        self.back_button = Button(BACK_BUTTON)
        self.back_button.set_pos(10,10)
        self.quit_button = Button(QUIT_BUTTON)
        self.quit_button.set_pos(10,10)
        self.replay_button = Button(REPLAY_BUTTON)
        self.replay_button.set_pos(340,350)
        self.rules_button = Button(RULES_BUTTON)
        self.rules_button.set_pos(340,350)

        self.failed_buttons = pygame.sprite.Group()
        self.failed_buttons.add(self.replay_button)

        self.start_buttons = pygame.sprite.Group()
        self.start_buttons.add(self.play_button)
        self.start_buttons.add(self.rules_button)

        self.rules_buttons = pygame.sprite.Group()
        self.rules_buttons.add(self.back_button)

        self.game_buttons = pygame.sprite.Group()
        self.game_buttons.add(self.quit_button)

      

        self.font_name = pygame.font.match_font('arial')

        self.total_score_font = pygame.font.Font(self.font_name, 72)
        self.other_font = pygame.font.Font(self.font_name, 30)

        

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True
        self.displaying_color = True
        
        self.backdrop1 = Backdrop("start_game")
        self.backdrop2 = Backdrop("rules")
        self.backdrop3 = Backdrop("game_page")
        self.backdrop4 = Backdrop("failed_page") 
       
       
        self.failed_backdrop = pygame.sprite.Group()
        self.failed_backdrop.add(self.backdrop4)

        self.game_backdrop = pygame.sprite.Group()
        self.game_backdrop.add(self.backdrop3)

        self.rules_backdrop = pygame.sprite.Group()
        self.rules_backdrop.add(self.backdrop2)

        self.start_backdrop = pygame.sprite.Group()
        self.start_backdrop.add(self.backdrop1)

        self.boxes = pygame.sprite.Group()
        self.boxes.add(self.green_box)
        self.boxes.add(self.yellow_box)
        self.boxes.add(self.blue_box)
        self.boxes.add(self.red_box)

    def reset_display(self):
        self.timer = 0
        self.displaying_color = True
        self.current_index = 0
        self.phase  = DISPLAY
        self.color_index = 0

    def reset_game(self):
        self.phase = START
        self.current_index = 0
        self.timer = 0
        self.time_limit = 40
        self.color_index = 0
        self.total_colors = 4
        self.total_score  = 0
        self.color_list = self.get_color_list(self.total_colors)



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

                elif color == GREEN:
                    self.green_box.activate()

                elif color == YELLOW:
                    self.yellow_box.activate()

                elif color == BLUE: 
                    self.blue_box.activate()


                if self.color_index == len(self.color_list):
                    self.displaying_color = False
                    self.phase = PLAY
            


    def update(self):
        """Updates the game"""
        self.clock.tick(FPS)

        self.screen.fill((255, 222, 222))

        if self.phase == DISPLAY:
            self.display_color_list()
        elif self.phase == PLAY:
            pass
        
        self.handle_input()

        if self.phase == START:
            self.start_backdrop.draw(self.screen)
            self.start_buttons.update()
            self.start_buttons.draw(self.screen)
        elif self.phase == RULES:
            self.rules_backdrop.update()
            self.rules_backdrop.draw(self.screen)   
            self.rules_buttons.update()
            self.rules_buttons.draw(self.screen)      
        elif self.phase == FAILED:
            self.failed_backdrop.update()
            self.failed_backdrop.draw(self.screen)             
            self.failed_buttons.update()
            self.failed_buttons.draw(self.screen)
            text_surface = self.total_score_font.render(str(self.total_score), True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (350, 200)
            self.screen.blit(text_surface, text_rect)

        elif self.phase == DISPLAY:
            self.boxes.update()
            self.boxes.draw(self.screen)
            self.game_buttons.update()
            self.game_buttons.draw(self.screen)
            text_surface = self.other_font.render("Watch the computer", True, (0,0,0))
            text_rect = text_surface.get_rect()                
            text_rect.midtop = (400, 550)

            self.screen.blit(text_surface, text_rect)

        elif self.phase == PLAY:
            self.boxes.update()
            self.boxes.draw(self.screen)
            self.game_buttons.update()
            self.game_buttons.draw(self.screen)
            text_surface = self.other_font.render("Your turn", True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (400, 550)
            self.screen.blit(text_surface, text_rect)
        
    




        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.phase == START:
                    pos =  pygame.mouse.get_pos()

                    for sprite in self.start_buttons:
                        if sprite.rect.collidepoint(pos):
                            if sprite.button_type == PLAY_BUTTON:
                                self.phase = DISPLAY

                            elif sprite.button_type  == RULES_BUTTON:
                                self.phase = RULES
                            
                elif self.phase == PLAY:
                    pos = pygame.mouse.get_pos()

                    for sprite in self.boxes:
                        if sprite.rect.collidepoint(pos):
                            sprite.activate()
                            if sprite.color == self.color_list[self.current_index]:
                                self.current_index += 1

                                if self.current_index == len(self.color_list):
                                    self.total_colors += 1
                                    self.color_list = self.get_color_list(self.total_colors)
                                    self.reset_display()
                                    self.total_score += 1
                
                            else:
                                self.phase = FAILED

                    for sprite in self.game_buttons:
                        if sprite.rect.collidepoint(pos):
                            if sprite.button_type == QUIT_BUTTON:
                                self.phase = START
                                self.reset_game()


                elif self.phase == RULES:
                    pos = pygame.mouse.get_pos()          
                    for sprite in self.rules_buttons:
                        if sprite.rect.collidepoint(pos):
                            if sprite.button_type == BACK_BUTTON:
                                self.phase = START


                elif self.phase == FAILED:
                    pos = pygame.mouse.get_pos()
                    for sprite in self.failed_buttons:
                        if sprite.rect.collidepoint(pos):
                            if sprite.button_type == REPLAY_BUTTON:
                                self.phase = START

                elif self.phase == DISPLAY:
                    pos = pygame.mouse.get_pos()
                    for sprite in self.game_buttons:
                        if sprite.rect.collidepoint(pos):
                            if sprite.button_type == QUIT_BUTTON:
                                self.phase = START
                                self.reset_game()

        
        
        

        # size = [300, 200]
        # screen = pygame.display.set_mode(size)



        
        
        
        done = False
        
        clock = pygame.time.Clock()
        
        font = self.other_font
        
        frame_count = 0
        frame_rate = 60
        start_time = 3
        

        while not done:
            for event in pygame.event.get():  #
                if event.type == pygame.quit:  
                    done = True  
        
           
            total_seconds = frame_count // frame_rate

            minutes = total_seconds // 60

            seconds = total_seconds % 60

            total_seconds = start_time - (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
        
            minutes = total_seconds // 60
            seconds = total_seconds % 60
        
            output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        
            text_surface = self.other_font(output_string, True, (0,0,0))

            
            text_rect = text_surface.get_rect()
            text_rect.midtop = (400, 550)
            self.screen.blit(text_surface, text_rect)
        
          

            frame_count += 1

            clock.tick(frame_rate)

            pygame.display.flip()

        pygame.quit()




                














def main():
    game = Game()

    while game.running:
        game.update()

if __name__ == '__main__':
    main()