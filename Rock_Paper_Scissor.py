import random

def play():

    my_choice = input("Choice 'r' for rock,'p' for paper, 's', for scissor ")
    computer = random.choice(['r', 'p', 's'])

    if my_choice == computer:
        print('Draw')
    if is_win(my_choice, computer):
        print('You won')
    if is_win(computer, my_choice):
        print('You lost')
 # r > s, s > p, p > r
 
def is_win(player, opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
play()