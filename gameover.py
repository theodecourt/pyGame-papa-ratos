from turtle import reset
import pygame
from config import *
from assets import *
from eskelleton import *
from pag_jogo import *


def perdeu(WINDOW):

    
    clock = pygame.time.Clock()
    assets = carrega_assets()
 
    
    state = GAMEOVER
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

        WINDOW.blit(assets[PAG_GAMEOVER], (0, 0))
       
        pygame.display.update()

    return state