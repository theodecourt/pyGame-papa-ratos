import pygame
pygame.init

class HEAD(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['roxocobra']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 
        self.speedx = 8
        self.speedy = 8
    
    def update(self):
        if keys_pressed[pygame.K_LEFT]: #left
            self.rect.x -= self.speedx
        if keys_pressed[pygame.K_RIGHT]: #right
            self.rect.x += self.speedx
        if keys_pressed[pygame.K_UP]: #up
            self.rect.y += self.speedy
        if keys_pressed[pygame.K_DOWN]: #down
            self.rect.y -= self.speedy

class RAT(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['rato']