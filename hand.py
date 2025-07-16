class Hand:
  def __init__(self):
    self.cards = []

  def __str__(self):
    return " ".join(str(card) for card in self.cards)

  def Add_Card(self, card):
    self.cards.append(card)

  def Calculate_Score(self):
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
    characters = [card.value for card in self.cards]
    total = sum([points[char] for char in characters if char != "A"])
    ace_count = characters.count("A")

    # Prioritises A to be 11
    for _ in range(ace_count):
      total += 11 if total + 11 <= 21 else 1

    return total
  
  def Clear(self):
    self.cards = []