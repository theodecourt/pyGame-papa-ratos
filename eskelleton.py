import pygame
import random
from config import *
from assets import *


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
        self.size = 0
    
    def update(self):
        self.rect.x += self.speedx  
        self.rect.y += self.speedy

'''class NEUTRO(pygame.sprite.Sprite):
    def __init__(self, assets, center):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEAD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        self.rect.center = center
    
    def update(self):
        pass        '''


class RAT(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[RAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-RATO_WIDTH)
        self.rect.y = random.randint(0, HEIGHT-RATO_HEIGHT)

class BODY(pygame.sprite.Sprite):
    def __init__(self, assets, center, neutro=True):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEAD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        self.rect.center = center
        self.neutro = neutro
    
    def update(self):
        pass        


with open(f'assets/mapa.csv', 'r') as arquivo:
    fase_lines = arquivo.readlines()
    separator = ','
    matriz_fase = []
    for linha in fase_lines:
        linha = linha.strip()
        linha = linha.split(separator)
        for i, block in enumerate(linha):
            linha[i] = block
            matriz_fase.append(linha)