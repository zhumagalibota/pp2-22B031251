import pygame
from pygame.locals import *
import random, time

pygame.init()

width, height = 400, 600
speed = 5
score, score_coins = 0, 0

#FONTS
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 15)
game_over = font.render("Game Over", True, (0, 0, 0))

#BACKGROUND
pygame.mixer.music.load("background.wav")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Street Racer")
background = pygame.image.load("AnimatedStreet.png")
clock = pygame.time.Clock()
'''
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        size = (30, 30)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), random.randint(40, height-40))

    def move(self):
        global score_coins
    ##    self.rect.move_ip(0, 0)
   #     if (self.rect.bottom > 600):
    #        score_coins += 1
      #  self.rect.center = (random.randint(70, 370), random.randint(70, 370))
'''

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

p1 = player()
e1 = enemy()
c1 = coin()

#GROUPS
enemies = pygame.sprite.Group()
enemies.add(e1)
coins = pygame.sprite.Group()
coins.add(c1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(c1)

#EVENT SPEED
speed_inc = pygame.USEREVENT + 1
pygame.time.set_timer(speed_inc, 1000)

running = True
if running:
        pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == speed_inc:
            speed += 0.5
        
        if event.type == pygame.QUIT:
            running = False
    #SCREEN 
    screen.blit(background, (0, 0))
    scores = font_small.render(f"Score: {str(score)}", True, (0, 0, 0))
    score_coins = font_small.render(f"Coins: {str(score)}", True, (0, 0, 0))
    screen.blit(scores, (10, 10))
    screen.blit(score_coins, (9, 30))


    #MOVING OBJECTS
    for i in all_sprites:
        screen.blit(i.image, i.rect)
        i.move()
    
    #COLLISION COINS
    if pygame.sprite.spritecollideany(p1, coins):
        score_coins += 1
        c1 = (random.randint(70, 370), random.randint(70, 370))
        pygame.display.flip()
        time.sleep(0.5)

    #COLLISION DETECTION
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.music.pause()
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)

        screen.fill((255, 0, 0))
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for i in all_sprites:
            i.kill()
        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(50)