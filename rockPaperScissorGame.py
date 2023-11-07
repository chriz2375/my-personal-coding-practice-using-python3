"""
Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. 
The program should work as follows: 
    1. When the program begins, a random number in the range of 1 through 3 is generated. 
    If the number is 1, then the computer has chosen rock. If the number is 2, then the computer 
    has chosen paper. If the number is 3, then the computer has chosen scissors. 
    (Don’t display the computer’s choice yet.)

    2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
    3. The computer’s choice is displayed. 
    4. A winner is selected according to the following rules: 
        •If one player chooses rock and the other player chooses scissors, 
        then rock wins. (The rock smashes the scissors.) 
        •If one player chooses scissors and the other player chooses paper, 
        then scissors wins. (Scissors cuts paper.)
        •If one player chooses paper and the other player chooses rock, 
        then paperwins. (Paper wraps rock.) 
        •If both players make the same choice, the game must be played again to determine the winner

"""

import random
TIE = 0
COMPUTER_WINS = 1
PLAYER_WINS = 2
INVALID = 3
ROCK = 1
PAPER = 2
SCISSOR = 3

def main():

    result = TIE
    while result == TIE:
        computer = random.randint(1, 3)
        player = int(input("Press 1 for Rock, 2 for Paper, and 3 for Scissor: \t"))

        print("The player choose {}".format(choices(player)))
        print("The computer choose {}".format(choices(computer)))

        result = rockPaperScissor(computer, player)

        if result == TIE:
            print("You both computer made the same choice. \n")

    if result == PLAYER_WINS:
        print("The player win. You win the game!")
    elif result == COMPUTER_WINS:
        print("The computer win the game! ")
    else:
        print("You made and invalid choice! No winner for this time.")



def rockPaperScissor(computer, player):
    if computer == player:
        return TIE
    
    elif computer == ROCK:
        if player == PAPER:
            return PLAYER_WINS
        elif player == SCISSOR:
            return COMPUTER_WINS
        else:
            return INVALID
        
    elif computer == PAPER:
        if player == ROCK:
            return COMPUTER_WINS
        elif player == SCISSOR:
            return PLAYER_WINS
        else:
            return INVALID

    else:
        if player == ROCK:
            return PLAYER_WINS
        elif player == PAPER:
            return COMPUTER_WINS
        else:
            return INVALID


def choices(choice):
    if choice == ROCK:
        return 'rock'
    elif choice == PAPER:
        return 'paper'
    elif choice == SCISSOR:
        return 'scissor'
    else:
        return 'Something went wrong'


main()


