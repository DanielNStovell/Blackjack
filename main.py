import pygame
import sys
from game import Game

background_colour = (40, 140, 50)

mul = 70

screen_width = 16 * mul
screen_height = 9 * mul
# Cards are 32x48 (width x height)
card_width = 32 * (mul * 0.06)
card_height = 48 * (mul * 0.06)

card_x_displacement = mul * (2/3)
card_y_displacement = mul * (2/3)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Backjack')
screen.fill(background_colour)
pygame.display.flip()
running = True

round = Game()
round.Start_New_Round()

player_cards = round.Get_Player_Hand()
print(player_cards)
image_list = []

class Sprites:
  def __init__(self, path):
    self.path = path
  
  def load(self):
    temp = pygame.image.load(self.path).convert_alpha()
    return pygame.transform.scale(temp, (card_width, card_height))

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# letters = ["J", "Q", "K", "A"]
# suits = "♠♥♦♣"
card_image_dict = {
  "A♠": "Cards/Spades/A_SPADE.png",
  "A♥": "Cards/Hearts/A_HEART.png",
  "A♦": "Cards/Diamonds/A_DIAMOND.png",
  "A♣": "Cards/Clovers/A_CLOVER.png",
  
  "6♠": "Cards/Spades/6_SPADE.png",
  "3♠": "Cards/Spades/3_SPADE.png"
}

player_cards = player_cards.split()

for card in player_cards:
  print(card)
  if card in card_image_dict:
    image_list.append(Sprites(card_image_dict[card]))
  else:
    image_list.append(Sprites("Cards/Clovers/A_CLOVER.png"))

player_card_center = (screen_width // 2) - ((len(player_cards) - 1) * (card_width + card_x_displacement))

while running:
  for idx, image in enumerate(image_list):
    screen.blit(image.load(),(idx * (card_width + card_x_displacement) + player_card_center, screen_height - card_height - card_y_displacement))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.flip()