import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_move())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's valid
            # if that spot is not available on the board, we also say it's invalid
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = True  # if these are successful, then awesome!
            except ValueError:
                print("Invalid square. Try again.")

        return val
