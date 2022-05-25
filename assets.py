import pygame
import os
from os import path
from config import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))


IMG_DIR = path.join(path.dirname(__file__), 'assets', 'imagens')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font') 

#imagens
CENARIO = 'cenario'
HEAD_IMG = 'cabeca'
BODY_IMG = 'body'
RAT_IMG = 'rato'
MAZE_WALLS1_IMG = 'paredes1'
MAZE_WALLS2_IMG = 'paredes2'
MAZE_WALLS3_IMG = 'paredes3'

#animacoes
EATING_ANIM = 'eating_anim'

#sons
NHAC_SOUND = 'eat_sound'
EW_SOUND = 'throwingup_sound'
BATIDA_SOUND = 'batida_sound'
DIE_SOUND = 'die_sound'


def carrega_assets():
    assets = {}
    assets[CENARIO] = pygame.image.load(os.path.join(IMG_DIR, 'cenario.png')).convert()
    assets[HEAD_IMG] = pygame.image.load(os.chdir(assets/imagens/'roxocobra.png')).convert_alpha()
    assets[HEAD_IMG] = pygame.transform.scale(assets[HEAD_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    assets[BODY_IMG] = pygame.image.load(os.path.join(IMG_DIR,'roxocobra.png')).convert_alpha()
    assets[BODY_IMG] = pygame.transform.scale(assets[BODY_IMG], (COBRA_WIDTH, COBRA_HEIGHT))
    assets[RAT_IMG] = pygame.image.load(os.path.join(IMG_DIR,'rato.png')).convert_alpha()
    assets[RAT_IMG] = pygame.transform.scale(assets[RAT_IMG], (RATO_WIDTH, RATO_HEIGHT))
    assets[MAZE_WALLS1_IMG] = pygame.image.load(os.path.join(IMG_DIR,'paredes1.png')).convert_alpha()
    assets[MAZE_WALLS1_IMG] = pygame.transform.scale(assets[MAZE_WALLS1_IMG], (PAREDE1_WIDTH, PAREDE1_HEIGHT))
    assets[MAZE_WALLS2_IMG] = pygame.image.load(os.path.join(IMG_DIR,'paredes2.png')).convert_alpha()
    assets[MAZE_WALLS2_IMG] = pygame.transform.scale(assets[MAZE_WALLS2_IMG], (PAREDE2_WIDTH, PAREDE2_HEIGHT))
    assets[MAZE_WALLS3_IMG] = pygame.image.load(os.path.join(IMG_DIR,'paredes3.png')).convert_alpha()
    assets[MAZE_WALLS3_IMG] = pygame.transform.scale(assets[MAZE_WALLS3_IMG], (PAREDE3_WIDTH, PAREDE3_HEIGHT))

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/sons/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    pygame.mixer.music.set_volume(0.4)
    assets[NHAC_SOUND] = pygame.mixer.Sound('assets/sons/cobracomendo.wav')
    assets[EW_SOUND] = pygame.mixer.Sound('assets/snd/expl6.wav')
    assets[BATIDA_SOUND] = pygame.mixer.Sound('assets/snd/pew.wav')
    assets[DIE_SOUND] = pygame.mixer.Sound('assets/snd/pew.wav')

    return assets