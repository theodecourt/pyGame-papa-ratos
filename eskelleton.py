
class HEAD(pygame.sprite.Sprite):
    def __init__(self, assets):
        self.image = 
        self.mask = 
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 
        self.speedx = 8
        self.speedy = 8
    
    def update(self):
        self.rect.y += self.speedy
        if keys_pressed[pygame.K_LEFT]: #left
            self.rect.x += self.speedx
        if keys_pressed[pygame.K_RIGHT] and cobra.x + VEL < WIDTH - (BORDER_DIAMETER + COBRA_WIDTH): #right
            cobra.x += VEL
        if keys_pressed[pygame.K_UP] and cobra.y - VEL > BORDER_DIAMETER: #up
            cobra.y -= VEL
        if keys_pressed[pygame.K_DOWN] and cobra.y + VEL < HEIGHT - (BORDER_DIAMETER + COBRA_HEIGHT): #down
            cobra.y += VEL
