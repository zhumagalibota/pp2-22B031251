import pygame
from pygame.locals import *
import random, time

pygame.init()

width, height = 400, 600
speed = 5
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Street Racer")
background = pygame.image.load("AnimatedStreet.png")
clock = pygame.time.Clock()

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
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
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

p1 = player()
e1 = enemy()

enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

speed_inc = pygame.USEREVENT + 1
pygame.time.set_timer(speed_inc, 1000)

running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == speed_inc:
            speed += 2

        if event.type == pygame.QUIT:
            running = False

    for i in all_sprites:
        screen.blit(i.image, i.rect)
        i.move()
    
    if pygame.sprite.spritecollideany(p1, enemies):
        screen.fill((255, 0, 0))
        pygame.display.update()
        for i in all_sprites:
            i.kill()
        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(50)