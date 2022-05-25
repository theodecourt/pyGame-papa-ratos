import pygame
from config import *
from assets import *
from eskelleton import *
import pag_jogo

pygame.init() 

#especificacoes tela
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAPA RATOS')

#texto
font = pygame.font.SysFont(None, 54)

#desenhar borda
def draw_border():
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER_LEFT)
    pygame.draw.rect(WINDOW, BLACK, BORDER_RIGHT)
    pygame.draw.rect(WINDOW, BLACK, BORDER_UP)
    pygame.draw.rect(WINDOW, BLACK, BORDER_DOWN)
    pygame.display.update()

#tela inicial
def tela_inicial():
    
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
        text = font.render('COMEÇAR (ENTER)', True, (0, 0, 255))
        text2 = font.render('SAIR (S)', True, (0, 0, 255))
        WINDOW.fill(GREEN)
        vertices = [(250, 100), (650, 100), (650, 200), (250, 200)]
        pygame.draw.polygon(WINDOW, BLACK, vertices)
        WINDOW.blit(text, (274, 135))
        vertices = [(250, 250), (650, 250), (650, 350), (250, 350)]
        pygame.draw.polygon(WINDOW, BLACK, vertices)
        WINDOW.blit(text2, (380, 285))
        pygame.display.update()
    
    return state


'''
def perdeu():
    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas
        window.fill((0,128,0))  # Preenche com a cor branca
        cor = (255, 255, 0)
        vertices = [(250, 0), (500, 200), (250, 400), (0, 200)]
        pygame.draw.polygon(window, cor, vertices)
        cor = ((0,0,139))
        pygame.draw.circle(window, cor, (250, 200), 100)
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador'''

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicial()
    elif state == GAME:
        state = pag_jogo()
    else:
        state = QUIT

pygame.quit()

