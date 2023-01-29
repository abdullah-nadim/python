import pygame
screen_size= [159,318]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load("download.jpg")
planet = pygame.image.load("images.jpg")
spaceship = pygame.image.load("")
bullet = pygame.image.load("")

keep_alive= True
while keep_alive:
    screen.blit(background,[0,0])
    screen.blit(planet,[90,30])
    screen.blit(bullet,[])
    screen.blit(spaceship,[])
    pygame.display.update()

