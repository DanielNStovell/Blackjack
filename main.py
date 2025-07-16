numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ["J", "Q", "K", "A"]
suits = "♠♥♦♣"

class LCG_Pseudo_Random_Generator:
  def __init__(self, seed=None):
    # Borland C/C++ Preset
    self.a = 22695477
    self.c = 1

    self.m = 2**31
    self.x0 = seed

    self.x_prev = (self.a * self.x0 + self.c) % self.m

  def generate_number(self, num_range=None):
    self.x_prev = (self.a * self.x_prev + self.c) % self.m
    
    if not num_range:
      return self.x_prev
    else:
      return int((self.x_prev / (self.m - 1)) * (num_range[1] + 1 - num_range[0]) + num_range[0])

"""
Cool seeds:
10 - Dealer gets natural blackjack on 2nd round
"""

seed = 10
lcg = LCG_Pseudo_Random_Generator(seed)

def Create_Deck():
  deck = []
  for number in numbers:
    for suit in suits:
      deck.append(f"{number}{suit}")
  for letter in letters:
    for suit in suits:
      deck.append(f"{letter}{suit}")
  return deck

def Shuffle_Cards(deck):
  deck_length = len(deck)

  for i in range(deck_length - 1, 0, -1): # Fisher-Yates shuffle
    j = lcg.generate_number() % (i + 1)
    deck[i], deck[j] = deck[j], deck[i]

  return deck

def Calculate_Hand(hand):
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
  }
  characters = [card[:-1] for card in hand]
  total = sum([points[char] for char in characters if char != "A"])
  ace_count = characters.count("A")

  # Prioritises A to be 11
  for _ in range(ace_count):
    if total + 11 <= 21:
      total += 11
    else:
      total += 1

  return total

def Draw(dealer_hand, player_hand, is_standing):
  print("\n"*10)
  # card_display_template = "#######\n#     #\n#     #\n#     #\n#     #\n#######"

  dealer_hand_display = dealer_hand.copy()

  if is_standing:
    dealer_hand_display[1] = "??"

  def Make_Card_Display(character, suit):
    center = f"# {character} {suit} #" if len(character) == 1 else f"# {character}{suit} #"
    return ["#######","#     #", center,"#     #","#     #","#######"]

  for hand in [dealer_hand_display, player_hand]:
    card_display_list = [Make_Card_Display(card[:-1], card[-1]) if card != "??" else 
                         ["#######", "#     #", "#  ?  #", "#     #", "#     #", "#######"] 
                         for card in hand]
    
    for row_idx in range(len(card_display_list[0])):
      row = " ".join(card[row_idx] for card in card_display_list)
      if row_idx == 2: # Middle row
        label = "Minimum" if is_standing and hand == dealer_hand_display else "Total"
        total = Calculate_Hand(hand if not (is_standing and hand == dealer_hand_display) else hand[:-1])
        row += f" {label}: {total}"
      print(row)
    print('\n')

def Play_Round():
  deck = Create_Deck()
  deck = Shuffle_Cards(deck)
  print(deck, "\n")

  dealer_hand = [deck[1], deck[3]]
  player_hand = [deck[0], deck[2]]
  next_card_idx = 4

  player_score = Calculate_Hand(player_hand)
  dealer_score = Calculate_Hand(dealer_hand)

  Draw(dealer_hand, player_hand, True)

  end = False

  # Checks for a natural blackjack
  if player_score == 21 and dealer_score != 21:
    Draw(dealer_hand, player_hand, False)
    print("You won")
    end = True
  elif player_score == 21 and dealer_score == 21:
    Draw(dealer_hand, player_hand, False)
    print("You draw")
    end = True
  elif dealer_score == 21:
    Draw(dealer_hand, player_hand, False)
    print("You lost")
    end = True

  while not end:
    print("1. hit\n2. stand")
    
    action = input("What do you do? (1, 2): ").strip()
    while action not in ["1", "2"]:
      print("Please enter either number 1 or 2!")
      action = input("What do you do? (1, 2): ").strip()
    
    if action == "1":
      if next_card_idx < len(deck):
        player_hand.append(deck[next_card_idx])
        next_card_idx += 1
      else:
        print("Deck is empty")
    elif action == "2":
      end = True
    else:
      print("Not an aciton")
      print("Enter number 1 or 2")
    
    player_score = Calculate_Hand(player_hand)

    if player_score > 21:
      end = True

    Draw(dealer_hand, player_hand, True)

    if end:
      # The dealer draws until they reach 17 or more (some blackjack rule)
      while dealer_score < 17 and next_card_idx < len(deck):
        dealer_hand.append(deck[next_card_idx])
        next_card_idx += 1
        dealer_score = Calculate_Hand(dealer_hand)

      Draw(dealer_hand, player_hand, False)
      player_score = Calculate_Hand(player_hand)
      dealer_score = Calculate_Hand(dealer_hand)

      if player_score > 21:
        print("You busted")
      elif dealer_score > 21:
        print("You won")
      elif player_score == 21:
        print("You got blackjack")
      elif player_score < dealer_score:
        print("You lost")
      elif player_score > dealer_score:
        print("You won")
      elif player_score == dealer_score:
        print("Draw")

if __name__ == "__main__":
  continue_playing = True
  while continue_playing:
    Play_Round()
    print("Do you want to play again?")
    print("1. Yes")
    print("2. No")
    play_again = input("Do you want to play again? (1, 2): ").strip()

    while play_again not in ["1", "2"]:
      print("Please enter either number 1 or 2!")
      play_again = input("Do you want to play again? (1, 2): ").strip()
    
    if play_again != "1":
      continue_playing = False
      print("Thank you for playing!")