import pygame   # ------------ not done yet

pygame.init()

pygame.mixer.music.load("EXO_-_Tempo_(musmore.com).mp3")
#songs = ["EXO_-_Tempo_(musmore.com).mp3", "BAEKHYUN_-_UN_Village_(musmore.com).mp3", "EXO_-_Ko_Ko_Bop_(musmore.com).mp3"]

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2 task")


running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_RIGHT] :
        pygame.mixer.music.play()
    elif keys[pygame.K_LEFT]:
        pygame.mixer.music.stop()
    elif keys[pygame.K_UP]:
        pygame.mixer.music.load("BAEKHYUN_-_UN_Village_(musmore.com).mp3")
        pygame.mixer.music.play()
    elif keys[pygame.K_DOWN]:
        pygame.mixer.music.load("EXO_-_Tempo_(musmore.com).mp3")
        pygame.mixer.music.play()
     

    pygame.display.flip()

