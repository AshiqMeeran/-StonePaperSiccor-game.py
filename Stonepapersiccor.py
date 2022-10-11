import random


def play():
    user = input("Enter 'r' for rock, 's' for siccor,  'p' for paper :")
    computer = random.choice(['r', 's', 'p'])
    if user == computer:
        return "tie"
    if is_win(computer, user):
        return 'You lose!'

    return 'You won!'


def is_win(player, opponent):
    if(player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 'r' and opponent == 'p'):
        return True


print(play())
