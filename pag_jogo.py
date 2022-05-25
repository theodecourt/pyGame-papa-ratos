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


    game = True
    while game:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:   #left
                    player.rect.x -= player.speedx
                if event.key == pygame.K_RIGHT: #right
                    player.rect.x += player.speedx
                if event.key == pygame.K_UP:       #up
                    player.rect.y -= player.speedy
                if event.key == pygame.K_DOWN:     #down
                    player.rect.y += player.speedy
            pygame.display.update()  # Mostra o novo frame para o jogador
        
        WINDOW.fill((0, 0, 0))  # Preenche com a cor branca
        all_sprites.draw(WINDOW)
        pygame.display.update()  # Mostra o novo frame para o jogador 