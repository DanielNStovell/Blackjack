from deck import Deck
from player import Player
from random_number import LCG_Pseudo_Random_Generator

class Game:
  def __init__(self):
    self.rng = LCG_Pseudo_Random_Generator(seed=10)
    self.deck = Deck(self.rng)
    self.player = Player("Player")
    self.dealer = Player("Dealer")
    self.state = "playing"  # 'playing', 'player_busted', 'dealer_busted', 'player_won', 'dealer_won', 'draw', 'blackjack'
    self.result = None

  def Start_New_Round(self):
    self.deck.Create()
    self.deck.Shuffle()
    
    self.player.hand.Clear()
    self.dealer.hand.Clear()

    self.state = "playing"
    self.result = None
    
    for _ in range(2):
      self.player.hand.Add_Card(self.deck.Deal())
      self.dealer.hand.Add_Card(self.deck.Deal())
    
    self.Check_Initial_Blackjack()

  def Check_Initial_Blackjack(self):
    player_score = self.player.hand.Calculate_Score()
    dealer_score = self.dealer.hand.Calculate_Score()
    
    if player_score == 21 and dealer_score != 21:
      self.state = "player_won"
      self.result = "You win"
    elif player_score == 21 and dealer_score == 21:
      self.state = "draw"
      self.result = "Draw"
    elif dealer_score == 21:
      self.state = "dealer_won"
      self.result = "You lost"

  def Player_Hit(self):
    if self.state != "playing":
      return

    if not self.deck.Is_Empty():
      self.player.hand.Add_Card(self.deck.Deal())
    
    player_score = self.player.hand.Calculate_Score()
    
    if player_score > 21:
      self.state = "player_busted"
      self.result = "You lost"
    elif player_score == 21:
      self.Player_Stand()

  def Player_Stand(self):
    if self.state != "playing":
      return
    
    # Dealer draws until 17 or more
    dealer_score = self.dealer.hand.Calculate_Score()

    while dealer_score < 17 and not self.deck.Is_Empty():
      self.dealer.hand.Add_Card(self.deck.Deal())
      dealer_score = self.dealer.hand.Calculate_Score()
    
    self.Determine_Winner()

  def Determine_Winner(self):
    player_score = self.player.hand.Calculate_Score()
    dealer_score = self.dealer.hand.Calculate_Score()

    if dealer_score > 21:
      self.state = "dealer_busted"
      self.result = "You win"
    elif player_score > 21:
      self.state = "player_busted"
      self.result = "You lost"
    elif player_score == 21:
      self.state = "player_won"
      self.result = "You win"
    elif player_score < dealer_score:
      self.state = "dealer_won"
      self.result = "You lost"
    elif player_score > dealer_score:
      self.state = "player_won"
      self.result = "You win"
    elif player_score == dealer_score:
      self.state = "draw"
      self.result = "Draw"

  def Get_Player_Hand(self):
    return str(self.player.hand)

  def Get_Dealer_Hand(self):
    return str(self.dealer.hand)

  def Get_Scores(self):
    return self.player.hand.Calculate_Score(), self.dealer.hand.Calculate_Score()

  def Is_Over(self):
    return self.state != "playing"

  def Get_Result(self):
    return self.result
  
  def Get_Chips(self):
    return self.chips