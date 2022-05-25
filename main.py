import pygame
from config import *
from assets import *
from eskelleton import *
from pag_inicial import *
from pag_jogo import *

pygame.init() 

#especificacoes tela
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAPA RATOS')


#desenhar borda
def draw_border():
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER_LEFT)
    pygame.draw.rect(WINDOW, BLACK, BORDER_RIGHT)
    pygame.draw.rect(WINDOW, BLACK, BORDER_UP)
    pygame.draw.rect(WINDOW, BLACK, BORDER_DOWN)
    pygame.display.update()

cobra = pygame.Rect(100, 300, COBRA_WIDTH, COBRA_HEIGHT)


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
        state = tela_inicial(WINDOW)
    elif state == GAME:
        state = pagina_jogo(WINDOW)
    else:
        state = QUIT

pygame.quit()

