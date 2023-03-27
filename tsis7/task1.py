import pygame

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('clock')
image = pygame.image.load('mickeyclock.jpeg').convert()
image = pygame.transform.scale(image, (600, 500))
done = False
while not done:
    screen.fill((250, 250, 250))
    screen.blit(image, (0, 0)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update() 

