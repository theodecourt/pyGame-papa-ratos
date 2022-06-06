import pygame
import random
from config import *
from assets import *


class HEAD(pygame.sprite.Sprite):
    def __init__(self, assets):
        
        pygame.sprite.Sprite.__init__(self)
        self.images = assets[explosao_animacao]
        self.image = assets[HEAD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.size = 0
        self.state = 1
        self.index_image = 0
    
    def update(self):
        if self.state == 1:
            self.rect.x += self.speedx  
            self.rect.y += self.speedy
        if self.state == 2:
            c = self.rect.center
            self.image = self.images[self.index_image]
            self.rect = self.image.get_rect()
            self.rect.center = c
            self.index_image += 1
            if self.index_image == len(self.images):
                self.state = 9


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
    def __init__(self, assets, x, y):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[RAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        
        #random.randint(0, WIDTH-RATO_WIDTH)
        #random.randint(0, HEIGHT-RATO_HEIGHT)
        

    def update(self):
        
        pass


'''class WALLS(pygame.sprite.Sprite):
    def __init__(self, assets, posx, posy):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['xxx']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(a, b)
        self.rect.y = random.randint(a, b)'''

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

class WALLS(pygame.sprite.Sprite):
    def __init__(self, assets, posx, posy):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['parede']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy
    def update(self):
        pass


class Explosao(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)


        self.animacao_explosao = assets[explosao_animacao]


        self.frame = 0
        self.image = self.animacao_explosao[self.frame] 
        self.rect = self.image.get_rect()
        self.rect.center = center  

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

        def update(self):

            agora = pygame.time.get_ticks()

            quantos_ticks_passaram = agora - self.last_update

            # Se já está na hora de mudar de imagem...
            if quantos_ticks_passaram > self.frame_ticks:
                # Marca o tick da nova imagem.
                self.last_update = agora

                # Avança um quadro.
                self.frame += 1

                # Verifica se já chegou no final da animação.
                if self.frame == len(self.animacao_explosao):
                    # Se sim, tchau explosão!
                    self.kill()
                else:
                    # Se ainda não chegou ao fim da explosão, troca de imagem.
                    center = self.rect.center
                    self.image = self.animacao_explosao[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
