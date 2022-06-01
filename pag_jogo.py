from re import S
import pygame
from config import *
from assets import *
from eskelleton import *
import time


def cria_labirinto(assets, all_sprites):    
    with open(f'assets/labirintos/labirinto1.csv', 'r') as arquivo:
        fase_lines = arquivo.readlines()
    all_walls = pygame.sprite.Group()
    for l in range(len(fase_lines)):
        for c in range(len(fase_lines[l])):
            e = fase_lines[l][c]
            if e == '1':
                w = WALLS(assets, c*SIZE, l*SIZE)
                all_walls.add(w)
                all_sprites.add(w)
    return all_walls

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
    all_bodies = pygame.sprite.Group()
    
    font = pygame.font.Font(None, 60)

    score = 0 

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bodies'] = all_sprites
    groups['all_rats'] = all_rats
    groups['maze_walls'] = maze_walls
    groups['all_neutros'] = all_sprites
    
    all_walls = cria_labirinto(assets, all_sprites)

    rat = RAT(assets)
    all_sprites.add(rat)
    all_rats.add(rat)


    clock = pygame.time.Clock()

    game = True
    while game:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    state = QUIT
                    game = False
            if event.type == pygame.KEYDOWN:
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
            placar = score
            game = False
            state = GAMEOVER
            
        
        c = player.rect.center
        all_sprites.update()  
        
        if len(all_bodies) < player.size:
            b = BODY(assets, c)
            all_sprites.add(b)
            all_bodies.add(b)
        elif len(all_bodies) == 0:
            pass
        else:
            all_bodies.sprites()[0].kill()
        for i in range(len(all_bodies)-5):
            all_bodies.sprites()[i].neutro = False


        papa_rato = pygame.sprite.spritecollide(player, all_rats, True, pygame.sprite.collide_mask)
        if len(papa_rato) > 0:
            assets[NHAC_SOUND].play()
            time.sleep(0.1)
            for rato in papa_rato:
                r = RAT(assets)
                all_sprites.add(r)
                all_rats.add(r)
                player.size += 1
                score += 1
        
        se_comeu = pygame.sprite.spritecollide(player, all_bodies, False, pygame.sprite.collide_mask)
        for body in se_comeu:
            if not body.neutro:
                placar = score
                state = GAMEOVER
                game = False
        
        WINDOW.fill(WHITE)  # Preenche com a cor branca

        all_sprites.draw(WINDOW)

        text_surface = assets[SCORE_FONTE].render("RATOS PAPADOS:  {}".format(score), True, (RED))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        WINDOW.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador 
    
    return state