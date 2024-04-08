import pygame
from settings import *
from personaje import Personaje
from balas import Bala
from meteorito import Meteorito

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.score = 0
        self.last_time_enemy = 0
        self.interval_enemies = 100
        self.last_time = 0
        self.interval = 50
        self.bala_added = False
        self.enemy_spawn = False
        self.enemy_collide = []
        
        self.enemy_speed = 5
        
        self.game_active = False
        self.game_over = False
        # Principal Player
        self.player = Personaje(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        # Sprites Groups for bullets and enemies
        self.bullets = pygame.sprite.Group()
        self.meteorites = pygame.sprite.Group()
    
    # Run our game
    def run(self):
        self.player.mover()
        self.player.dibujar(self.display_surface)
        self.player.draw_hearts(self.display_surface)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.bala_added:
            bullet = Bala(self.player.rect.centerx, self.player.rect.centery, self.player.rotation)
            self.bullets.add(bullet) 
            self.bala_added = True
        
        if not self.enemy_spawn:
            # Enemy spawn
            meteorite = Meteorito(self.player.rect.center, self.enemy_speed)
            self.meteorites.add(meteorite)
            self.enemy_spawn = True
        
        self.bullets.update()
        self.meteorites.update()

        self.bullets.draw(self.display_surface)
        self.meteorites.draw(self.display_surface)
        
        enemy_destroyed = pygame.sprite.groupcollide(self.meteorites, self.bullets, True, True)
        self.enemy_coll = pygame.sprite.spritecollide(self.player, self.meteorites, True)
        
        if len(enemy_destroyed)>0:
            # Increased the score when hit an enemy with a bullet
            self.score +=1
        if len(self.enemy_coll) > 0:
            # The player take a hit bc an enemy collide
            self.player.hit() 
            
        if self.last_time > self.interval:
            self.bala_added = False
            self.last_time = 0
            
        if self.last_time_enemy > self.interval_enemies:
            self.enemy_spawn = False
            self.last_time_enemy = 0
        
        self.last_time += 1
        self.last_time_enemy += 1
    
    def win_level(self, score):
        if score >= 5:
            return True
        else:
            return False
        
        
        
    def init_next_level(self, diff_interval_enemies, plus_speed_enemy):
        self.__init__()
        self.interval_enemies -= diff_interval_enemies
        self.enemy_speed += plus_speed_enemy
        