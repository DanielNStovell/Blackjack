from card import Card

class Deck:
  def __init__(self, rng):
    self.cards = []
    self.rng = rng

  def Create(self):
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    letters = ["J", "Q", "K", "A"]
    suits = "♠♥♦♣"

    self.cards = [Card(str(character), suit) for character in numbers + letters for suit in suits]

  def Shuffle(self):
    deck_length = len(self.cards)

    for i in range(deck_length - 1, 0, -1): # Fisher-Yates shuffle
      j = self.rng.Generate_Number() % (i + 1)
      self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
  
  def Deal(self):
    return self.cards.pop()
  
  def Is_Empty(self):
    return not self.cards