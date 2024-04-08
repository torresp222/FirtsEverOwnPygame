import pygame

class Start_Menu:
    def __init__(self, font: pygame.font.Font) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = font
        self.is_mouse_button = False
        self.color_text_button = 'yellow'
        
        self.start_text = self.font.render('Hit start button to start the game',True, 'yellow')
        self.start_text = pygame.transform.scale(self.start_text,(1000,100))
        self.start_text_rect = self.start_text.get_rect(center = (640,200))
        
        self.level_one = self.font.render('LEVEL 1',True, 'yellow')
        self.level_one = pygame.transform.scale(self.level_one,(200,80))
        self.level_one_rect = self.level_one.get_rect(center = (640,310))
        
        self.button = pygame.Surface((40,40))
        self.button =  pygame.transform.scale(self.button,(400,100))
        self.button_rect = self.button.get_rect(center = (640,450))
        
        self.fill_rect = 1  
    
    def draw(self):
        self.text_button = self.font.render('START',True, self.color_text_button)
        self.text_button_rect = self.text_button.get_rect(center = (640,450))
        
        pygame.draw.rect(self.display_surface,"yellow", self.button_rect,self.fill_rect)
        self.display_surface.blit(self.start_text, self.start_text_rect)
        self.display_surface.blit(self.level_one, self.level_one_rect)
        self.display_surface.blit(self.text_button, self.text_button_rect)
    
    def  hover_mouse(self, pos):
        if pos[0] in range(self.button_rect.left, self.button_rect.right) and pos[1] in range(self.button_rect.top, self.button_rect.bottom):
            self.fill_rect = 0
            self.color_text_button = 'black'
            self.is_mouse_button = True
        else:
            self.fill_rect = 1
            self.color_text_button = 'yellow'
            self.is_mouse_button = False
            
    def click_start_game(self, clicked):
        if clicked and self.is_mouse_button:
            return True
        else:
            return False

class GameOver_Menu:
    def __init__(self, font: pygame.font.Font, score: int, level) -> None:
        self.font = font
        self.is_mouse_button = False
        self.color_text_button = 'yellow'
        
        self.level = level
        
        self.start_text = self.font.render('Game Over',True, 'yellow').convert_alpha()
        self.start_text = pygame.transform.scale(self.start_text,(400,100))
        self.start_text_rect = self.start_text.get_rect(center = (640,200))
        
        self.level_text = self.font.render(f'Level {self.level}',True, 'yellow').convert_alpha()
        self.level_text = pygame.transform.scale(self.level_text,(200,80))
        self.level_text_rect = self.level_text.get_rect(center = (580,320))
        
        self.score_text = self.font.render(str(score),True, 'yellow')
        self.score_text_rect = self.score_text.get_rect(center = (700,320))
        
        self.button = pygame.Surface((40,40))
        self.button =  pygame.transform.scale(self.button,(400,100))
        self.button_rect = self.button.get_rect(center = (640,450))
        
        self.fill_rect = 1
    
    def draw(self, surface: pygame.Surface):
        self.text_button = self.font.render('RESTART',True, self.color_text_button)
        self.text_button_rect = self.text_button.get_rect(center = (640,450))
        
        pygame.draw.rect(surface,"yellow", self.button_rect,self.fill_rect)
        surface.blit(self.start_text, self.start_text_rect)
        surface.blit(self.level_text, self.level_text_rect)
        surface.blit(self.score_text, self.score_text_rect)
        surface.blit(self.text_button, self.text_button_rect)
    
    def  hover_mouse(self, pos):
        if pos[0] in range(self.button_rect.left, self.button_rect.right) and pos[1] in range(self.button_rect.top, self.button_rect.bottom):
            self.fill_rect = 0
            self.color_text_button = 'black'
            self.is_mouse_button = True
        else:
            self.fill_rect = 1
            self.color_text_button = 'yellow'
            self.is_mouse_button = False
            
    def click_start_game(self, clicked):
        if clicked and self.is_mouse_button:
            return True
        else:
            return False
        
class NextLevel_Menu:
    def __init__(self, font: pygame.font.Font, score: int, level) -> None:
        self.font = font
        self.is_mouse_button = False
        self.color_text_button = 'yellow'
        self.level = level
        
        self.start_text = self.font.render(f'Level {self.level}',True, 'yellow').convert_alpha()
        self.start_text = pygame.transform.scale(self.start_text,(400,100))
        self.start_text_rect = self.start_text.get_rect(center = (640,200))
        
        self.score_text = self.font.render(str(score),True, 'yellow')
        self.score_text_rect = self.score_text.get_rect(center = (640,320))
        
        self.button = pygame.Surface((40,40))
        self.button =  pygame.transform.scale(self.button,(400,100))
        self.button_rect = self.button.get_rect(center = (640,450))
        
        self.fill_rect = 1
    
    def draw(self, surface: pygame.Surface):
        self.text_button = self.font.render('NEXT LEVEL',True, self.color_text_button)
        self.text_button_rect = self.text_button.get_rect(center = (640,450))
        
        pygame.draw.rect(surface,"yellow", self.button_rect,self.fill_rect)
        surface.blit(self.start_text, self.start_text_rect)
        surface.blit(self.score_text, self.score_text_rect)
        surface.blit(self.text_button, self.text_button_rect)
    
    def  hover_mouse(self, pos):
        if pos[0] in range(self.button_rect.left, self.button_rect.right) and pos[1] in range(self.button_rect.top, self.button_rect.bottom):
            self.fill_rect = 0
            self.color_text_button = 'black'
            self.is_mouse_button = True
        else:
            self.fill_rect = 1
            self.color_text_button = 'yellow'
            self.is_mouse_button = False
            
    def click_start_game(self, clicked):
        if clicked and self.is_mouse_button:
            return True
        else:
            return False