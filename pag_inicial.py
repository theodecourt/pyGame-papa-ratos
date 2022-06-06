import pygame
from config import *
from assets import *
from eskelleton import *

def pagina_inicial(WINDOW):

    
    clock = pygame.time.Clock()
    assets = carrega_assets()
    
    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    state = QUIT
                    game = False
            
                if event.key == pygame.K_RETURN:
                    state = GAME
                    game = False
                    

        WINDOW.fill(GREEN)
        WINDOW.blit(assets[PAG_INICIAL], (0, 0))

        pygame.display.update()
    
    return state