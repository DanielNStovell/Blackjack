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

card_x_displacement = mul * (1/3)
card_y_displacement = mul * (2/3)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Backjack')
pygame.display.flip()
running = True

round = Game()
round.Start_New_Round()

player_cards = round.Get_Player_Hand().split()

class Card_Sprite:
  def __init__(self, path, x, y):
    self.path = path

    self.x, self.y = x, y
  
  def load(self, cw=card_width, ch=card_height):
    temp = pygame.image.load(self.path).convert_alpha()
    return pygame.transform.scale(temp, (cw, ch))
  
  def check_hover(self, card_width, card_height):
    mouseX, mouseY = pygame.mouse.get_pos()
    return self.x <= mouseX <= self.x + card_width and self.y <= mouseY <= self.y + card_height

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

def Load_Card_Image():
  card_display_list = []
  num_cards = len(player_cards)
  total_width = num_cards * card_width + (num_cards - 1) * card_x_displacement
  start_x = (screen_width - total_width) // 2
  for idx, card in enumerate(player_cards):
    if card in card_image_dict:
      path = card_image_dict[card]
    else:
      path = "Cards/Missing.png"

    x = start_x + idx * (card_width + card_x_displacement)
    y = screen_height - card_height - card_y_displacement
    card_display_list.append(Card_Sprite(path, x, y))
  return card_display_list

round.Player_Hit()
player_cards = round.Get_Player_Hand().split()

while running:
  screen.fill(background_colour)
  for idx, card in enumerate(Load_Card_Image()):
    base_width = card_width
    base_height = card_height
    if card.check_hover(base_width, base_height):
      draw_width = base_width * 1.1
      draw_height = base_height * 1.1
    else:
      draw_width = base_width
      draw_height = base_height
    
    card_x_center = (draw_width - base_width) / 2
    card_y_center = (draw_height - base_height) / 2
    
    pygame.draw.circle(screen, (0, 255, 0), (card.x, card.y), 5)
    pygame.draw.circle(screen, (0, 255, 0), (card.x + card_width, card.y), 5)

    card_image = card.load(draw_width, draw_height)
    screen.blit(card_image, (card.x - card_x_center, card.y - card_y_center))

    pygame.draw.circle(screen, (255, 0, 0), (screen_width//2, screen_height//2), 20)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()