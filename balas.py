import pygame
import settings as st

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, dir) -> None:
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        
        pygame.draw.circle(self.image, "green",(self.image.get_width()/2, self.image.get_height()/2),8)
        self.dir = dir
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def update(self):
        self.rect.move_ip(self.dir.x*10, self.dir.y*10)
        
        if self.rect.top < 0 or self.rect.top > st.SCREEN_HEIGHT:
            self.kill()
        if self.rect.left < 0 or self.rect.left > st.SCREEN_WIDTH:
            self.kill()