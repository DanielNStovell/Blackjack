# Blackjack Game

A simple command-line Blackjack game written in Python without external libraries.

## Features

- Complete deck creation and shuffling
- Player and dealer turns
- Proper Blackjack scoring (Aces = 1 or 11)
- Dealer draws until reaching 17+ (standard rules)
- Win/lose/draw detection

## How to Play

1. Run the game: `python BJ.py`
2. You'll see your cards and the dealer's first card
3. Choose to "hit" (1) or "stand" (2)
4. The dealer will play their hand after you stand
5. See who wins!

## Game Rules

- Get as close to 21 as possible without going over
- Face cards (J, Q, K) = 10 points
- Aces = 1 or 11 (automatically optimized)
- Dealer must draw until reaching 17 or more
- You win if you have a higher score than the dealer (without busting)

## Requirements

- Python 3.x (no external libraries needed)

## Files

- `main.py` - Main game file 
