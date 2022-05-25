import pygame
import random

class HEAD(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['HEAD_IMAGE']
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

        self.image = assets['RAT_IMAGE']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(a, b)
        self.rect.y = random.randint(a, b)


class WALLS(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['xxx']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(a, b)
        self.rect.y = random.randint(a, b)
