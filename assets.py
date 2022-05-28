import pygame
import os
from os import path
from config import *
#os.chdir(os.path.dirname(os.path.abspath(_file_)))

#IMG_DIR = path.join(path.dirname(_file_), 'assets', 'imagens')
#SND_DIR = path.join(path.dirname(_file_), 'assets', 'sons')
#FNT_DIR = path.join(path.dirname(_file_), 'assets', 'font') 

#imagens
CENARIO = 'cenario'
HEAD_IMG = 'cabeca'
BODY_IMG = 'body'
RAT_IMG = 'rato'


#animacoes
EATING_ANIM = 'eating_anim'

#sons
NHAC_SOUND = 'eat_sound'
EW_SOUND = 'throwingup_sound'
BATIDA_SOUND = 'batida_sound'
DIE_SOUND = 'die_sound'


def carrega_assets():
    assets = {}
    #assets[CENARIO] = pygame.image.load(os.path.join(IMG_DIR, 'cenario.png')).convert()
    assets[HEAD_IMG] = pygame.image.load('assets/imagens/roxooficial.png').convert_alpha()
    assets[HEAD_IMG] = pygame.transform.scale(assets[HEAD_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    assets[BODY_IMG] = pygame.image.load('assets/imagens/roxooficial.png').convert_alpha()
    assets[BODY_IMG] = pygame.transform.scale(assets[BODY_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    assets[RAT_IMG] = pygame.image.load('assets/imagens/rato.png').convert_alpha()
    assets[RAT_IMG] = pygame.transform.scale(assets[RAT_IMG], (RATO_WIDTH, RATO_HEIGHT))


    # Carrega os sons do jogo
    #pygame.mixer.music.load('assets/sons/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    #pygame.mixer.music.set_volume(0.4)
    assets[NHAC_SOUND] = pygame.mixer.Sound('assets/sons/cobracomendo.wav')
    #assets[EW_SOUND] = pygame.mixer.Sound('assets/snd/expl6.wav')
    #assets[BATIDA_SOUND] = pygame.mixer.Sound('assets/snd/pew.wav')
    #assets[DIE_SOUND] = pygame.mixer.Sound('assets/snd/pew.wav')

    return assets