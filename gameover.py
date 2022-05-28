import pygame
from config import *
from assets import *
from eskelleton import *

def perdeu(WINDOW):

    #texto
    font = pygame.font.SysFont(None, 54)
    font2 = pygame.font.SysFont(None, 70)
    clock = pygame.time.Clock()
    #assets = carrega_assets()
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = GAME
                    game = False
        text = font.render('JOGAR DE NOVO (ENTER)', True, (0, 0, 255))
        text2 = font.render('SAIR (S)', True, (0, 0, 255))
        text_gameover = font2.render('GAMEOVER)', True, (0, 0, 255))
        WINDOW.fill(GREEN)
        vertices = [(250, 100), (650, 100), (650, 200), (250, 200)]
        pygame.draw.polygon(WINDOW, BLACK, vertices)
        WINDOW.blit(text, (274, 135))
        vertices = [(250, 250), (650, 250), (650, 350), (250, 350)]
        pygame.draw.polygon(WINDOW, BLACK, vertices)
        WINDOW.blit(text2, (380, 285))
        WINDOW.blit(text_gameover, 350, 100)
        pygame.display.update()
    
    return state