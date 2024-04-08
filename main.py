import pygame
import sys
import settings as st
from menus import Start_Menu, GameOver_Menu, NextLevel_Menu
from ui import UI
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SpaceShip Survival")
        
        self.screen = pygame.display.set_mode((st.SCREEN_WIDTH,st.SCREEN_HEIGHT))
        self.myfont = pygame.font.SysFont("monospace", 50)
        self.ven_half_x = self.screen.get_width() / 2
        self.ven_half_y = self.screen.get_height() / 2
        self.clock = pygame.time.Clock()
        self.run_game = True
        self.click = False
        self.dt = 0
        
        self.start_menu = Start_Menu(self.myfont)
        self.ui = UI(self.myfont)
        
        self.level = Level()
        self.game_active = self.level.game_active
        self.game_over = self.level.game_over
        self.win_level = False
        self.win_game = False
        self.next_menu_level = False
        
        self.plus_interval = 10
        self.speed_enemy_upgrade = 1

        self.level_game = 1
        

    def run(self):
        # Game run
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True
                else:
                    self.click = False
            
            if self.game_active:   
                self.screen.fill("black")
                self.ui.display_score(self.level.score)
                self.game_over = self.level.player.is_dead()
                self.level.run()
                self.win_level = self.level.win_level(self.level.score)
                
                if self.win_level:
                    self.level_game += 1
                    self.next_menu_level = True
                    self.win_level = False
                    self.game_active = False
                
                if self.game_over:
                    self.game_active = False
            else:
                
                if not self.win_level and self.next_menu_level:
                    menu_mouse_pos = pygame.mouse.get_pos()
                    next_level_menu = NextLevel_Menu(self.myfont, self.level.score, self.level_game)
                    self.screen.fill("black")
                    next_level_menu.hover_mouse(menu_mouse_pos)
                    next_level_menu.draw(self.screen)
                    self.game_active = next_level_menu.click_start_game(self.click)
                    
                    if self.game_active:
                        self.level.init_next_level(self.plus_interval, self.speed_enemy_upgrade)
                        self.plus_interval += 10
                        self.speed_enemy_upgrade += 1
                        self.next_menu_level = False
                        
                elif self.game_over:
                    menu_mouse_pos = pygame.mouse.get_pos()
                    game_over_menu = GameOver_Menu(self.myfont, self.level.score, self.level_game)
                    self.screen.fill("black")
                    game_over_menu.hover_mouse(menu_mouse_pos)
                    game_over_menu.draw(self.screen)
                    self.game_active = game_over_menu.click_start_game(self.click)
                    
                    if self.game_active:
                        self.level.__init__()
                else:
                    menu_mouse_pos = pygame.mouse.get_pos()
                    self.screen.fill("black")
                    self.start_menu.hover_mouse(menu_mouse_pos) 
                    self.start_menu.draw()
                    self.game_active = self.start_menu.click_start_game(self.click)
            
            pygame.display.update()
            self.dt = self.clock.tick(60) / 1000
    

if __name__ == "__main__":
    game = Game()
    game.run()