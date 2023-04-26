import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
image  = pygame.image.load("main-clock.png")
image = pygame.transform.scale(image, (500, 500))
screen.blit(image, (0, 0))
clock = pygame.time.Clock()
min_hand = pygame.image.load("right-hand.png")
sec_hand = pygame.image.load("left-hand.png")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)
