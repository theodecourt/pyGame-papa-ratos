import pygame
from config import *
from assets import *
from eskelleton import *
from pag_jogo import *

def perdeu(WINDOW):

    #texto MAS SEPA NAO PRECISA DISSO
    #font = pygame.font.SysFont(None, 54)
    #font2 = pygame.font.SysFont(None, 70)

    
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
        text_gameover = assets[GAMEOVER_FONTE].render('GAMEOVER', True, (0, 0, 255))
        text_playagain = assets[TELAINICIAL_FONTE].render("PLAY AGAIN (PRESS ENTER)", True, (BLACK)) #VER SE PCS DO PARENTESES
        text_sair = assets[TELAINICIAL_FONTE].render("QUIT (PRESS S)", True, (BLACK)) #VER SE PCS DO PARENTESES
        WINDOW.fill(RED)
        vertices = [(250, 100), (500, 100), (500, 200), (250, 200)]
        pygame.draw.polygon(WINDOW, WHITE, vertices)
        vertices = [(250, 250), (650, 250), (650, 350), (250, 350)]
        pygame.draw.polygon(WINDOW, WHITE, vertices)
        WINDOW.blit(text_gameover, (300, 50))
        WINDOW.blit(text_playagain, (300, 150))
        WINDOW.blit(text_sair, (300, 300))


        texto_res = assets[SCORE_FONTE].render("VOCE PAPOU {} RATOS!".format(placar), True, (BLACK))
        text_rect = texto_res.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        WINDOW.blit(texto_res, text_rect)
        
        pygame.display.update()

    return state