import random


def guess(x):
    random_number = random.randint(1, x)
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input(f"Enter a guess number between 1 and {x}: "))
        guess_count += 1
        if guess == random_number:
            print("Congratulations, You won!")
            break
        elif guess > random_number:
            print('Your guess number is above the wanted number!')
        elif guess < random_number:
            print('Your guess number is below the wanted number! ')
    else:
        print("Oh, sorry; you're wrong and your given time to guess has been elapsed!")
    print("You can kindly take your time to play next time. Thanks!")


guess(10)
