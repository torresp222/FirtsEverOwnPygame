import pygame
from settings import *

class UI:
    def __init__(self, font: pygame.font.Font) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = font
    
    def display_score(self, score):
        score_text = self.font.render(str(score), True, "yellow")
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH -50, 50))
        self.display_surface.blit(score_text,score_rect)