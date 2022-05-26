from re import S
import pygame
from config import *
from assets import *
from eskelleton import *



def pagina_jogo(WINDOW):
#SPRITES

    assets = carrega_assets()

    all_sprites = pygame.sprite.Group()
    player = HEAD(assets)
    all_sprites.add(player)
    #body = pygame.sprite.Group()
    all_rats = pygame.sprite.Group()
    maze_walls = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['body'] = all_sprites
    groups['all_rats'] = all_rats
    groups['maze_walls'] = maze_walls

    rat = RAT(assets)
    all_sprites.add(rat)
    all_rats.add(rat)

    clock = pygame.time.Clock()
    direita = 0
    esquerda = 0
    cima = 0
    baixo = 0

    game = True
    while game:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    state = QUIT
                    game = False
                if event.key == pygame.K_s:
                    state = QUIT
                    game = False
                if event.key == pygame.K_LEFT:   #left
                    esquerda = 1
                    direita = 0
                    baixo = 0
                    cima = 0
                if event.key == pygame.K_RIGHT: #right
                    esquerda = 0
                    direita = 1
                    baixo = 0
                    cima = 0
                if event.key == pygame.K_UP:       #up
                    esquerda = 0
                    direita = 0
                    baixo = 0
                    cima = 1
                if event.key == pygame.K_DOWN:     #down
                    esquerda = 0
                    direita = 0
                    baixo = 1
                    cima = 0
            pygame.display.update()  # Mostra o novo frame para o jogador
        if cima == 1 :
            player.speedy -= VEL
        if direita == 1:
            player.speedx += VEL
        if esquerda == 1 :
            player.speedx -= VEL
        if baixo == 1 :
            player.speedy += VEL
        WINDOW.fill(WHITE)  # Preenche com a cor branca
        all_sprites.draw(WINDOW)
        pygame.display.update()  # Mostra o novo frame para o jogador 