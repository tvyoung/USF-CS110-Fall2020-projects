# lets the user play the game of Rock, Paper, Scissors against the computer.
import random

#global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
	#creates result variable and sets it to 0 in order for the while loop to run. 
	result = 0
	#while loop should continue to run as long as result = 0, or as long as there is a tie
	while result == 0:
		#asks the user to choose rock, paper, or scissors 
		player = int(input("enter 1 for rock, 2 for paper, 3 for scissors: "))
		#generate a random number between 1 and 3 for the computer
		#1 = rock, 2 = paper, 3 = scissors
		computer = random.randint(1,3)

		#calls choiceString(choice) function to print computer's hand
		print("computer chose", choiceString(computer))
		#calls choiceString(choice) function to print player's hand
		print("player chose", choiceString(player))

		#calls function rockPaperScissors(computer, player) to get the result of the round between the computer and player and stores it in variable "result"
		result = rockPaperScissors(computer, player)

		#if result is 1, the computer wins
		if result == 1:
			print("the computer wins the game!")
		#if the result is 2, the player wins
		elif result == 2:
			print("you win the game!")
		#if the result is 3, the player has entered an invalid answer, and there is no winner. does not loop again
		elif result == 3:
			print("you made an invalid choice. no winner.")
		#if the result is 0, the game is a tie, and the while loop repeats again.
		elif result == 0:
			print("you made the same choice as the computer! starting over")
		#if the result is 1, 2, or 3, breaks the while loop and ends the game. 


#takes in integers representing the computer and player’s ‘hand’ so to speak of rock, paper, or scissors as arguments
#returns either TIE, COMPUTER_WINS, PLAYER_WINS, or INVALID.
def rockPaperScissors(computer, player):
	#if player chose rock(1)
	if player == ROCK:
		#if computer also chose rock(1)
		if computer == ROCK:
			return TIE
		#if computer chose paper(2)
		elif computer == PAPER:
			return COMPUTER_WINS
		#if computer chose scissors(3)
		elif computer == SCISSORS:
			return PLAYER_WINS
	#if player chose paper(2)
	elif player == PAPER:
		#if computer chose rock(1)
		if computer == ROCK:
			return PLAYER_WINS
		#if computer also chose paper(2)
		elif computer == PAPER:
			return TIE
		#if computer chose scissors(3)
		elif computer == SCISSORS:
			return COMPUTER_WINS
	#if player chose scissors(3)
	elif player == SCISSORS:
		#if computer also chose rock(1)
		if computer == ROCK:
			return COMPUTER_WINS
		#if computer chose paper(2)
		elif computer == PAPER:
			return PLAYER_WINS
		#if computer also chose scissors(3)
		elif computer == SCISSORS:
			return TIE
	#if player chose anything other than 1, 2, or 3, returns invalid
	else: 
		return INVALID


#takes in the argument choice (the number representing rock, paper, or scissors) and return either corresponding string value of the given integer argument
def choiceString(choice):
	#if the argument is 1, returns "rock"
	if choice == 1:
		return "rock"
	#if the argument is 2, returns "paper"
	elif choice == 2:
		return "paper"
	#if the argument is 3, returns scissors"
	elif choice == 3:
		return "scissors"
	#if the argument is not 1, 2, or 3, returns an error message
	else:
		return "something went wrong"


main()