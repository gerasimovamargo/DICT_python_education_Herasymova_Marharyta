"""Dominoes is a family of tile-based games played with rectangular "domino" tiles. Each domino is a rectangular tile"""

# Libraries
import random
from itertools import combinations_with_replacement
from random import shuffle


class Dominos:
    def __init__(self):
        """Initialize the game with 28 tiles, 7 tiles for each player and 14 tiles in the stock.
        The tiles are shuffled."""
        self.tiles: list = list(combinations_with_replacement(range(0, 7), 2))
        self.tiles: list = [list(tile) for tile in self.tiles]
        shuffle(self.tiles)
        self.stock_tiles: list = self.tiles[:len(self.tiles) // 2]
        self.pc_tiles: list = self.tiles[len(self.tiles) // 2:len(self.tiles) * 3 // 4]
        self.player_tiles: list = self.tiles[len(self.tiles) * 3 // 4:]
        self.table_tiles: list = []
        self.snake = None
        self.status = None
        self.pc_input = None

    def snake_check(self):
        """Check the highest double in the player's and computer's tiles."""
        doubles = [tile for tile in self.pc_tiles + self.player_tiles if tile[0] == tile[1]]
        if doubles:
            highest_double = max(doubles)
            if highest_double in self.player_tiles:
                self.player_tiles.remove(highest_double)
                self.status = 'PC'
            else:
                self.pc_tiles.remove(highest_double)
                self.status = 'Player'
            self.snake = highest_double

    def game_interface(self):
        """Print the game interface."""
        print('=' * 70)
        print('Stock size:', len(self.stock_tiles))
        print('Computer pieces:', len(self.pc_tiles))
        print("Snake:", self.snake)
        print(*self.table_tiles, '\n', sep='') if len(self.table_tiles) <= 6 else \
            print(*self.table_tiles[:3], '...', *self.table_tiles[-3:], '\n', sep='')
        print("Player pieces:")
        for i, tile in enumerate(self.player_tiles):
            print(f"{i + 1}:[{tile[0]}, {tile[1]}]")
        print(f"Status:{self.status}")
        print('=' * 70)

    def computer_move(self):
        """Define the computer's move."""
        if self.status == 'PC':
            self.pc_input = random.randint(-len(self.pc_tiles), len(self.pc_tiles))

    def make_a_move(self, m, pieces):
        """Define the player's move"""
        if m > 0:
            domino = pieces[m - 1]
            right_snake = int(self.table_tiles[-1][4])
            if domino.count(right_snake) > 0:
                if right_snake == domino[1]:
                    domino = [domino[1], domino[0]]
                self.table_tiles.append(str(domino))
                del pieces[m - 1]
            else:
                return 'Illegal'
        if m < 0:
            domino = pieces[-m - 1]
            left_snake = int(self.table_tiles[0][1])
            if left_snake in domino:
                if left_snake == domino[0]:
                    domino = [domino[1], domino[0]]
                self.table_tiles.insert(0, str(domino))
                del pieces[-m - 1]
            else:
                return 'Illegal'
        if m == 0:
            if self.stock_tiles:
                pieces.append(self.stock_tiles.pop(0))

    def game_process(self):
        """Start the game process."""
        self.snake_check()
        self.table_tiles.append(str(self.snake))
        while True:
            self.game_interface()
            if self.status == 'Player':
                if not self.player_tiles:
                    self.status = 'PC'
                    continue
                while True:
                    try:
                        user_input = int(input("Enter your choice:"))
                    except ValueError:
                        print('Invalid input. Please try again.')
                        continue
                    if int(user_input) not in range(-len(self.player_tiles), len(self.player_tiles) + 1):
                        print('Invalid input. Please try again.')
                        continue
                    if self.make_a_move(int(user_input), self.player_tiles) == 'Illegal':
                        print('Illegal move. Please try again.')
                        continue
                    break
                self.status = 'PC'
            elif self.status == 'PC':
                print("\nStatus: It's the computer's turn to make a move.")
                while True:
                    self.computer_move()
                    if self.make_a_move(self.pc_input, self.pc_tiles) == 'Illegal':
                        continue
                    break
                self.status = 'Player'
            if self.table_tiles[0][1] == self.table_tiles[-1][4] and "".join(self.table_tiles).count(
                    self.table_tiles[0][1]) == 8:
                print("Draw!")
                exit()
            if len(self.player_tiles) == 0:
                print("You win!")
                exit()
            if len(self.pc_tiles) == 0:
                print("Computer wins!")
                exit()


# Main
if __name__ == '__main__':
    dominoes = Dominos()
    dominoes.game_process()
