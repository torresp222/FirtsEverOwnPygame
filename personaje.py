import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        
        self.display_surface = pygame.display.get_surface()
        
        self.image = pygame.image.load("./Images/cohete.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.rotation = pygame.Vector2(0, -1)
        self.direction = pygame.Vector2()
        
        self.angle = 2
        self.angle_rot = 0
        self.speed = 3
        self.life = 5
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
           self.direction.y = -1
        elif keys[pygame.K_DOWN]:
           self.direction.y = 1
        else:
            self.direction.y = 0
                  
        if keys[pygame.K_LEFT]:
           self.direction.x = -1 
        elif keys[pygame.K_RIGHT]:
           self.direction.x = 1
        else:
            self.direction.x = 0       
            
    def mover(self):
        self.input()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.center += self.direction * self.speed
         
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.rotation = self.rotation.rotate(self.angle)
            self.angle_rot -= self.angle
            self.rotar()
        if keys[pygame.K_q]:
            self.rotation = self.rotation.rotate(-self.angle)
            self.angle_rot += self.angle
            self.rotar()
           
    def rotar(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle_rot,1)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def dibujar(self, surface):
        self.display_surface.blit(self.image, self.rect)
        # pygame.draw.rect(surface,"yellow", self.rect,1)
    
    def is_dead(self):
        if self.life <= 0:
            return True
        else:
            return False
         
    def hit(self):
        self.life -= 1
        self.is_dead()
    
    def draw_hearts(self, surface):
        for heart in range(self.life):
            x = 30 + heart * 40
            y = 30
            h = Heart((x, y))
            surface.blit(h.image, h.rect)


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load("Images/corazon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(20,20))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=pos)