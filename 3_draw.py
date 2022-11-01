import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
color = (255, 255, 255)
screen.fill(color)

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 5)
rect(screen, (0, 0, 0), (150, 225, 100, 30))
rect(screen, (255, 0, 0), (150, 225, 100, 30), 5)
circle(screen, (0, 0, 0), (160, 170), 15)
circle(screen, (0, 0, 0), (240, 170), 15)
circle(screen, (255, 0, 0), (160, 170), 5)
circle(screen, (255, 0, 0), (240, 170), 5)
line(screen, (0, 0, 0), (140, 140), (180, 150), 7)
line(screen, (0, 0, 0), (260, 140), (220, 150), 7)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()