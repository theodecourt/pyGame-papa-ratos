import pygame

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAPA RATOS')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 30

RATO_WIDTH, RATO_HEIGHT = 30, 30
COBRA_WIDTH, COBRA_HEIGHT = 30, 30

RATO_IMG = pygame.image.load('cobra2.png').convert() #colocar nome da imagem do rato
RATO_PEQUENO_IMG = pygame.transform.scale(RATO_IMG, (RATO_WIDTH, RATO_HEIGHT))
COBRA_IMG = pygame.image.load('cobrinha.png').convert() #colocar nome da imagem do cobra
COBRA_PEQUENA_IMG = pygame.transform.scale(COBRA_IMG, (COBRA_WIDTH, COBRA_HEIGHT))

def draw_window(red, yellow):
    WINDOW.fill(WHITE)
    WINDOW.blit(RATO_PEQUENO_IMG, (yellow.x, yellow.y))
    WINDOW.blit(COBRA_PEQUENA_IMG, (red.x, red.y))
    pygame.display.update()

red = pygame.Rect(100, 300, RATO_WIDTH, RATO_HEIGHT)
yellow = pygame.Rect(100, 300, COBRA_WIDTH, COBRA_HEIGHT)

clock = pygame.time.Clock()
game = True
while game:    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        draw_window(red, yellow)
        
    red.x += 1


pygame.quit()