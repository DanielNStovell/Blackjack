from hand import Hand

class Player:
  def __init__(self, name):
    self.name = name
    self.hand = Hand()

  def __str__(self):
    return f"{self.name}: {self.hand} Total: {self.hand.Calculate_Score()}"