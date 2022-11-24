from art import logo
from replit import clear
import random

def deal ():
	"""Add a new card to the list of cards"""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def check_scores(sum_cards):
	"""Calculates scores"""
	if 11 in sum_cards and 10 in sum_cards and len(sum_cards) == 2:
		return 0
	if 11 in sum_cards and sum(sum_cards) > 21:
		sum_cards.remove(11)
		sum_cards.append(1)	
	return sum(sum_cards)

def compare (player_score, computer_score):
	"""Compares scores of player and computer"""
	if computer_score == 0:
		print(f"\nOpponent has a Black Jack You lost!")
	elif player_score == 0:
		print(f"\nYou have a Black Jack. You won!")
	elif player_score > 21:
		print(f"\nOh no {player_score}, you went over 21. You lost!")
	elif computer_score > 21:
		print(f"\nWith a score of: {computer_score} your opponent went over 21. That was easy. You won!")
	elif player_score == computer_score:
		print(f"\nYou both scored the same {player_score}. It is a draw!")
	elif player_score > computer_score:
		print(f"\nOpponent: {computer_score}. You won! with a score of: {player_score}")
	elif computer_score > player_score:
		print(f"\nYou lost! with {player_score} against oppoenent score {computer_score}")

def play():
	print(logo)
	computer_cards = []
	player_cards = []
	game_over = False

	for _ in range (2):
		player_cards.append(deal())
		computer_cards.append(deal())

	while game_over is not True:

		computer_score = check_scores(computer_cards)
		player_score = check_scores(player_cards)
	
		print(f"Computer first card is: [{computer_cards[0]}]")
		print(f"Your cards are: {player_cards} Your score is: {player_score}")
		
		if computer_score == 0 or player_score == 0 or player_score > 21:
			game_over = True
		else:
			new_card = input("Would you like to add a new card? Type 'y' for yes and 'n' for no: ").lower()
			if new_card == 'y':
				clear()
				print(logo)
				player_cards.append(deal())
			else:
				game_over = True
				
	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal())
		computer_score = check_scores(computer_cards)

	compare(player_score, computer_score)


if input("Would you like to play Black Jack? Type 'y' for yes and 'n' for no. ").lower() == 'y':
	clear()
	play()
	
while input("\nAnother turn? Type 'y' or 'n': ") == "y":
  clear()
  play()