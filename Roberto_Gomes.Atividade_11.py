import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.jumping = False
        self.sprites_walk = []
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0
        self.vel_y = 0
        self.flip = False
        
        # Walking animation
        self.sprites_walk.append(pygame.image.load("Assets/mario_andando1.png"))
        self.sprites_walk.append(pygame.image.load("Assets/mario_andando2.png"))
        self.sprites_walk.append(pygame.image.load("Assets/mario_andando3.png"))
        self.sprites_walk.append(pygame.image.load("Assets/mario_andando4.png"))

        # Jumping animation
        self.sprites_jump = []
        self.sprites_jump.append(pygame.image.load("Assets/mario_andando1.png"))
        self.sprites_jump.append(pygame.image.load("Assets/mario_pulando1.png"))
        self.sprites_jump.append(pygame.image.load("Assets/mario_pulando2.png"))
        
        self.current_sprite = 0
        self.image = self.sprites_walk[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        
    def update(self, speed):
        if not jump:
            if anim == True:
                self.current_sprite += speed
            
                if self.current_sprite >= len(self.sprites_walk):
                    self.current_sprite = 0

                if not self.flip:
                    self.image = self.sprites_walk[int(self.current_sprite)]
                else:
                    self.image = pygame.transform.flip(self.sprites_walk[int(self.current_sprite)], True, False)
        else:
             if anim == True:
                self.current_sprite += speed
            
                if self.current_sprite >= len(self.sprites_jump):
                    self.current_sprite = 0
                    
                if not self.flip:
                    self.image = self.sprites_jump[int(self.current_sprite)]
                else:
                    self.image = pygame.transform.flip(self.sprites_jump[int(self.current_sprite)], True, False)
        

                
    # Função para detectar se o player está no ar
    def falling(self):
        self.pos_y += 6
            

            
    def jump(self):
        self.pos_y -= 15
        
        
        
    def move(self, flip):
        if not self.jumping:
            # Detecta se o player virou para assim virar o seu sprite
            if flip:
                self.vel_x = -3
                self.flip = True
            else:
                self.vel_x = 3
                self.flip = False

                
pygame.init()
clock = pygame.time.Clock()

# Boleano para mostrar que a animação está rodando 
anim = False
pos = 0
jump = False

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player(200, 200)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
                anim = True
                
            if event.key == pygame.K_RIGHT:
                player.move(False)
                anim = True
                
                
            if event.key == pygame.K_LEFT:
                player.move(True)
                anim = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                anim = False
                player.vel_x = 0
                
            if event.key == pygame.K_LEFT:
                anim = False
                player.vel_x = 0
    
    # Evita que o player fique no ar           
                   
    player.pos_x += player.vel_x

    if player.pos_y < 100:
        jump = False
        anim = False
        
    if jump:
        player.jump()
        player.jumping = True
    else:
        player.jumping = False
        
        
    if player.pos_y < 200 and player.jumping == False: 
        player.falling()
    elif player.pos_y > 200:
        player.pos_y = 200
    
    
    screen.fill((0, 0, 0))

    
    if not anim and player.current_sprite != 0:
        player.current_sprite = 0
        if player.flip:
            player.image = pygame.transform.flip(player.sprites_walk[int(player.current_sprite)], True, False)
        else:
            player.image = player.sprites_walk[int(player.current_sprite)]
    else:
        moving_sprites.update(0.3)

        
    screen.blit(player.image, (player.pos_x, player.pos_y))
    pygame.display.flip()
    clock.tick(60)
    
