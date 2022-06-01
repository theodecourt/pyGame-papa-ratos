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

