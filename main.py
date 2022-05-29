import pygame
from config import *
#from assets import *
from eskelleton import *
from pag_inicial import *
from pag_jogo import *
from gameover import *

pygame.init() 
pygame.mixer.init()

#especificacoes tela
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAPA RATOS')


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
        state = pagina_inicial(WINDOW)
    elif state == GAME:
        state = pagina_jogo(WINDOW)
    elif state == GAMEOVER:
        state == perdeu(WINDOW)
    else:
        state = QUIT

pygame.quit()

