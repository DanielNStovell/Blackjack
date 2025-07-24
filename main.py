import pygame
import sys
from game import Game

pygame.init()

background_colour = (0, 100, 0)

mul = 80

screen_width = 16 * mul
screen_height = 9 * mul

# Cards are 32x48 (width x height)
card_width = 32 * (mul * 0.05)
card_height = 48 * (mul * 0.05)

card_x_displacement = mul * (1/3)
card_y_displacement = mul * (2/3)

# Board is 180x320 (width x height)
board_width = screen_width
board_height = screen_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Backjack')
pygame.display.flip()
running = True

round = Game()
round.Start_New_Round()

player_cards = round.Get_Player_Hand().split()
dealer_cards = round.Get_Dealer_Hand().split()
print(player_cards)
print(dealer_cards)

class Card_Sprite:
  def __init__(self, path, x, y):
    self.path = path

    self.x, self.y = x, y

    self.scale = 1.0
  
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
  "Back": "Cards/Back.png",

  "A♠": "Cards/Spades/A_SPADE.png",
  "A♥": "Cards/Hearts/A_HEART.png",
  "A♦": "Cards/Diamonds/A_DIAMOND.png",
  "A♣": "Cards/Clovers/A_CLOVER.png",
  
  "2♠": "Cards/Spades/2_SPADE.png",
  "3♠": "Cards/Spades/3_SPADE.png",
  "4♠": "Cards/Spades/4_SPADE.png",
  "5♠": "Cards/Spades/5_SPADE.png",
  "6♠": "Cards/Spades/6_SPADE.png",
  "7♠": "Cards/Spades/7_SPADE.png",
  "8♠": "Cards/Spades/8_SPADE.png",
  "9♠": "Cards/Spades/9_SPADE.png",
  "10♠": "Cards/Spades/10_SPADE.png",
  "J♠": "Cards/Spades/J_SPADE.png",
  "Q♠": "Cards/Spades/Q_SPADE.png",
  "K♠": "Cards/Spades/K_SPADE.png",

  "2♥": "Cards/Hearts/2_HEART.png",
  "3♥": "Cards/Hearts/3_HEART.png",
  "4♥": "Cards/Hearts/4_HEART.png",
  "5♥": "Cards/Hearts/5_HEART.png",
  "6♥": "Cards/Hearts/6_HEART.png",
  "7♥": "Cards/Hearts/7_HEART.png",
  "8♥": "Cards/Hearts/8_HEART.png",
  "9♥": "Cards/Hearts/9_HEART.png",
  "10♥": "Cards/Hearts/10_HEART.png",
  "J♥": "Cards/Hearts/J_HEART.png",
  "Q♥": "Cards/Hearts/Q_HEART.png",
  "K♥": "Cards/Hearts/K_HEART.png",

  "2♦": "Cards/Diamonds/2_DIAMOND.png",
  "3♦": "Cards/Diamonds/3_DIAMOND.png",
  "4♦": "Cards/Diamonds/4_DIAMOND.png",
  "5♦": "Cards/Diamonds/5_DIAMOND.png",
  "6♦": "Cards/Diamonds/6_DIAMOND.png",
  "7♦": "Cards/Diamonds/7_DIAMOND.png",
  "8♦": "Cards/Diamonds/8_DIAMOND.png",
  "9♦": "Cards/Diamonds/9_DIAMOND.png",
  "10♦": "Cards/Diamonds/10_DIAMOND.png",
  "J♦": "Cards/Diamonds/J_DIAMOND.png",
  "Q♦": "Cards/Diamonds/Q_DIAMOND.png",
  "K♦": "Cards/Diamonds/K_DIAMOND.png",

  "2♣": "Cards/Clovers/2_CLOVER.png",
  "3♣": "Cards/Clovers/3_CLOVER.png",
  "4♣": "Cards/Clovers/4_CLOVER.png",
  "5♣": "Cards/Clovers/5_CLOVER.png",
  "6♣": "Cards/Clovers/6_CLOVER.png",
  "7♣": "Cards/Clovers/7_CLOVER.png",
  "8♣": "Cards/Clovers/8_CLOVER.png",
  "9♣": "Cards/Clovers/9_CLOVER.png",
  "10♣": "Cards/Clovers/10_CLOVER.png",
  "J♣": "Cards/Clovers/J_CLOVER.png",
  "Q♣": "Cards/Clovers/Q_CLOVER.png",
  "K♣": "Cards/Clovers/K_CLOVER.png",
}

def Load_Player_Card_Image():
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

def Load_Dealer_Card_Image():
  card_display_list = []
  num_cards = len(dealer_cards)
  total_width = num_cards * card_width + (num_cards - 1) * card_x_displacement
  start_x = (screen_width - total_width) // 2

  new_dealer_cards = dealer_cards
  if not round.Is_Over():
    new_dealer_cards = dealer_cards[:-1]
    new_dealer_cards.append("Back")

  for idx, card in enumerate(new_dealer_cards):
    if card in card_image_dict:
      path = card_image_dict[card]
    else:
      path = "Cards/Missing.png"

    x = start_x + idx * (card_width + card_x_displacement)
    y = 0 + card_y_displacement
    card_display_list.append(Card_Sprite(path, x, y))
  return card_display_list

"""
round.Player_Hit()
player_cards = round.Get_Player_Hand().split()
"""

def Draw_Cards(hand):
  normal_scale = 1.0
  hover_scale = 1.1

  if hand == "Player":
    loaded_cards = Load_Player_Card_Image()
  elif hand == "Dealer":
    loaded_cards = Load_Dealer_Card_Image()

  for card in loaded_cards:
    if card.check_hover(card_width, card_height) and hand == "Player":
      scale = hover_scale
    else:
      scale = normal_scale

    card.scale = scale

    draw_width = card_width * card.scale
    draw_height = card_height * card.scale

    card_x_center = (draw_width - card_width) / 2
    card_y_center = (draw_height - card_height) / 2

    card_image = card.load(draw_width, draw_height)

    if hand == "Player":
      screen.blit(card_image, (card.x - card_x_center, card.y - card_y_center))
    elif hand == "Dealer":
      card_image = pygame.transform.rotate(card_image, 180)
      screen.blit(card_image, (card.x - card_x_center, card.y - card_y_center))

    pygame.draw.circle(screen, (0, 255, 0), (card.x, card.y), 5)
    pygame.draw.circle(screen, (0, 255, 0), (card.x + card_width, card.y), 5)

def Dealer_Minimum(hand):
  points = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": "11/1"
  }
  card = str(hand.cards[0])
  return points[card[:-1]]

Failed = pygame.mixer.Sound("Sounds/Failed.mp3")
Successed = pygame.mixer.Sound("Sounds/Successed.mp3")
Draw = pygame.mixer.Sound("Sounds/Win.mp3")

def Outcome_Sound():
  print(round.Is_Over())
  if round.Is_Over():
    print(round.Get_Result())
    if round.Get_Result() == "You win":
      pygame.mixer.Sound.play(Successed)
    elif round.Get_Result() == "You lost":
      pygame.mixer.Sound.play(Failed)
    else:
      pygame.mixer.Sound.play(Draw)

font = pygame.font.Font('freesansbold.ttf', 32)

chip_amount = 100
chip_amount_text = font.render(f'Chips: {chip_amount}', True, (255, 255, 255))
chip_amount_textRect = chip_amount_text.get_rect()
chip_amount_textRect.bottomright = (screen_width-len(f"{chip_amount}")*10 + 5, screen_height - 7)

board = pygame.image.load("Sprites/Board.png").convert_alpha()
board = pygame.transform.scale(board, (board_width, board_height))

while running:
  screen.fill(background_colour)

  screen.blit(board, (0, 0))

  Draw_Cards("Player")
  Draw_Cards("Dealer")

  screen.blit(chip_amount_text, chip_amount_textRect)

  pygame.draw.circle(screen, (255, 0, 0), (screen_width//2, screen_height//2), 20)

  player_total = round.player.hand.Calculate_Score()
  dealer_total = round.dealer.hand.Calculate_Score()
  player_total_text = font.render(f'Player total: {player_total}', True, (255, 255, 255))
  dealer_total_text = font.render(f'Dealer minimum: {Dealer_Minimum(round.dealer.hand)}' if not round.Is_Over() else f'Dealer total: {dealer_total}', True, (255, 255, 255))
  player_total_textRect = player_total_text.get_rect()
  dealer_total_textRect = dealer_total_text.get_rect()
  player_total_textRect.center = (screen_width // 2, screen_height - 25)
  dealer_total_textRect.center = (screen_width // 2, 25)
  screen.blit(player_total_text, player_total_textRect)
  screen.blit(dealer_total_text, dealer_total_textRect)

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and not round.Get_Result():
        round.Player_Hit()
        player_cards = round.Get_Player_Hand().split()
        print(dealer_cards)
        print(player_cards)
        Outcome_Sound()
      elif event.key == pygame.K_e and not round.Get_Result():
        round.Player_Stand()
        dealer_cards = round.Get_Dealer_Hand().split()
        print(dealer_cards)
        print(player_cards)
        Draw_Cards("Dealer")
        Outcome_Sound()
      elif event.key == pygame.K_SPACE and round.Get_Result():
        round.Start_New_Round()
        player_cards = round.Get_Player_Hand().split()
        dealer_cards = round.Get_Dealer_Hand().split()
        Outcome_Sound() # Checks for initial blackjack

    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()