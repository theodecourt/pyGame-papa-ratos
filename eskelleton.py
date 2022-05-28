import pygame
import random
from config import *
from assets import *
from eskelleton import *


class HEAD(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEAD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.rect.x += self.speedx  
        self.rect.y += self.speedy


class RAT(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[RAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-RATO_WIDTH)
        self.rect.y = random.randint(0, HEIGHT-RATO_HEIGHT)


'''class WALLS(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['xxx']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(a, b)
        self.rect.y = random.randint(a, b)'''
