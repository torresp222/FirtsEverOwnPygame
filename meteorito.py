from typing import Any
import pygame
import random
import settings as st

class Meteorito(pygame.sprite.Sprite):
    def __init__(self, dir, speed) -> None:
        super().__init__()
        self.image = pygame.image.load("Images/meteorito.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.original_image = self.image
        self.rect = self.image.get_rect()
        
        self.rect.center = self.generar_tupla()
        
        self.direccion = (0, 0)
        self.direccion = (self.rect.centerx - dir[0], self.rect.centery - dir[1])
        self.dir = pygame.Vector2(self.direccion[0],self.direccion[1]).normalize()
        
        self.speed = speed
        
        self.surface = pygame.display.get_surface()
        
    
    def update(self):
        self.rect.move_ip(-(self.dir.x*self.speed), -(self.dir.y*self.speed))
        # pygame.draw.rect(self.surface,"yellow", self.rect,1)
        if self.rect.top < 0 or self.rect.top > st.SCREEN_HEIGHT:
            self.kill()
        if self.rect.left < 0 or self.rect.left > st.SCREEN_WIDTH:
            self.kill()
            
            
    def generar_tupla(self):
        # Rangos para la coordenada x
        x_ranges = [(0, st.SCREEN_WIDTH_QUARTER), (st.SCREEN_WIDTH_QUARTER*3, st.SCREEN_WIDTH)]
        # Rangos para la coordenada y
        y_ranges = [(0, st.SCREEN_HEIGHT_QUARTER), (st.SCREEN_HEIGHT_QUARTER*3, st.SCREEN_HEIGHT)]

        # Seleccionar un rango aleatorio para x y y
        x_range = random.choice(x_ranges)
        y_range = random.choice(y_ranges)

        # Generar números aleatorios dentro de los rangos seleccionados
        x = random.randint(x_range[0], x_range[1])
        y = random.randint(y_range[0], y_range[1])

        return (x, y)