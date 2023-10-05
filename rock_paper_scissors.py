import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    # s < r, p < s, r < p
    if is_win(user, computer):
        return "You won!"
    else:
        return "You lost!"


def is_win(player, opponent):
    # s < r, p < s, r < p
    if (player == 'r', opponent == 's') or (player == 's', opponent == 'p') or (player == 'p', opponent == 'r'):
        return True


print(play())
