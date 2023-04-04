import pygame

pygame.init()

width, height = 500, 500
screen  = pygame.display.set_mode((width, height))
pygame .display.set_caption("Paint")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)