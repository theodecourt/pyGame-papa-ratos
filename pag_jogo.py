from re import S
import pygame
from config import *
from assets import *
from eskelleton import *
import time

def pagina_jogo(WINDOW):
#SPRITES
    state = GAME
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
                if event.type == pygame.QUIT:
                    state = QUIT
                    game = False
                if event.key == pygame.K_s:
                    state = QUIT
                    game = False
                if event.key == pygame.K_LEFT and player.speedx != VEL and player.speedx != -VEL:     #left
                    player.speedx -= VEL     
                    player.speedy = 0       
                if event.key == pygame.K_RIGHT and player.speedx != -VEL and player.speedx != VEL:    #right
                    player.speedx += VEL
                    player.speedy = 0   
                if event.key == pygame.K_UP and player.speedy != VEL and player.speedy != -VEL:       #up
                    player.speedy -= VEL
                    player.speedx = 0   
                if event.key == pygame.K_DOWN and player.speedy != -VEL and player.speedy != VEL:     #down
                    player.speedy += VEL
                    player.speedx = 0   
                    
        if player.rect.x < 0 or player.rect.x > (WIDTH - COBRA_WIDTH) or player.rect.y < 0 or player.rect.y > (HEIGHT - COBRA_HEIGHT):
            game = False
            state = INIT
            

        all_sprites.update()  

        papa_rato = pygame.sprite.spritecollide(player, all_rats, True, pygame.sprite.collide_mask)
        
        if len(papa_rato) > 0:
            assets[NHAC_SOUND].play()
            time.sleep(0.1)
            for rato in papa_rato:
                r = RAT(assets)
                all_sprites.add(r)
                all_rats.add(r)
            

        WINDOW.fill(WHITE)  # Preenche com a cor branca
        all_sprites.draw(WINDOW)
        pygame.display.update()  # Mostra o novo frame para o jogador 
    
    return state