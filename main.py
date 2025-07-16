import pygame
import sys
from game import Game

background_colour = (50, 135, 0)

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Backjack')

screen.fill(background_colour)

pygame.display.flip()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False