import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("3 task")

x, y = 25, 25
v = 1 # 20 пикселей это сколько?

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 500-25:
        x += v
    elif keys[pygame.K_LEFT] and x > 25:
        x -= v
    elif keys[pygame.K_UP] and y > 25:
        y -= v
    elif keys[pygame.K_DOWN] and y < 500-25:
        y += v

    c = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25) 

    pygame.display.flip()

