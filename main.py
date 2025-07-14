numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ["J", "Q", "K", "A"]
suits = "♠♥♦♣"

def Create_Deck():
  deck = []
  for number in numbers:
    for suit in suits:
      deck.append(f"{number}{suit}")
  for letter in letters:
    for suit in suits:
      deck.append(f"{letter}{suit}")
  return deck

def Random_Number():
  seed = id(1) ^ id(2) ^ id(3) # Increase entropy 
  seed = (seed * 134856 + 82745) % (2**32) # LCG formula
  return seed

def Shuffle_Cards(deck):
  deck_length = len(deck)

  for i in range(deck_length - 1, 0, -1): # Fisher-Yates shuffle
    j = Random_Number() % (i + 1)
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

deck = Create_Deck()
deck = Shuffle_Cards(deck)
print(deck, "\n")

other_hand = [deck[1], deck[3]]
player_hand = [deck[0], deck[2]]
next_card_idx = 4

end = False

while not end:
  print(' '.join(other_hand[:-1]), "?", "\n")
  print(' '.join(player_hand))
  print("your total:", Calculate_Hand(player_hand))
  print("1. hit\n2. stand")
  action = input("What do you do? (1, 2): ")
  if action == "1":
    player_hand.append(deck[next_card_idx])
    next_card_idx += 1
  elif action == "2":
    end = True
  else:
    print("Not an aciton")
    print("Enter number 1 or 2")

# The dealer draws until they reach 17 or more (some blackjack rule)
while Calculate_Hand(other_hand) < 17:
  other_hand.append(deck[next_card_idx])
  next_card_idx += 1

print(' '.join(other_hand))
print(' '.join(player_hand))

if Calculate_Hand(player_hand) > 21:
  print("You busted")
elif Calculate_Hand(player_hand) == 21:
  print("You got blackjack")
elif Calculate_Hand(player_hand) < Calculate_Hand(other_hand):
  print("You lost")
elif Calculate_Hand(player_hand) > Calculate_Hand(other_hand):
  print("You won")
elif Calculate_Hand(player_hand) == Calculate_Hand(other_hand):
  print("Draw")