"""Rock, Paper, Scissors game with the ability to play with the computer"""

# Libraries
import random
import json
import os


class RockPaperScissors:
    """Initialize the class and create the necessary variables"""

    def __init__(self):
        self.user_input = None
        self.easy_level = ["rock", "paper", "scissors"]
        self.hard_level = ["rock", "paper", "scissors", "lizard", "spock", "zombie", "gun", "lightning", "devil",
                           "dragon", "water", "air", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]
        self.name = ""
        self.score = 0
        self.pc_input = None
        self.signs = []
        self.winners = None

    def load_results(self):
        """Load the results from a file in JSON format."""
        if os.path.exists("results.txt"):
            with open("results.txt", "r") as f:
                results = json.load(f)
                name = self.name
                if name in results:
                    scores = [result['score'] for result in results[name]]
                    self.score += sum(scores)

    def save_results(self):
        """Save the results to a file in JSON format. If the file does not exist, create it."""
        with open("results.txt", "w") as f:
            json.dump({}, f)

        with open("results.txt", "r") as f:
            results = json.load(f)

        name = self.name
        score = self.score
        game = len(results.get(name, [])) + 1 if name in results else 1

        if name not in results:
            results[name] = []
        results[name].append({"game": game, "score": score})

        with open("results.txt", "w") as f:
            json.dump(results, f, indent=4)

    def show_results(self):
        """Show the results of the player and the number of attempts. If the file does not exist, display a message."""
        if not os.path.exists("results.txt"):
            print("No results found.")
            return

        with open("results.txt", "r") as f:
            results = json.load(f)

        name = self.name

        if name not in results:
            print("No results found for this player.")
            return

        print(f"Results for {name}:")
        for result in results[name]:
            print(f"Total points after the game  {result['game']}: {result['score']}")

    def levels(self):
        """Choose the level of the game."""
        print("Choose your level:")
        print("1. Easy")
        print("2. Hard")
        self.user_input = input("Enter your choice: ")
        if self.user_input == "1":
            self.level_easy()
        elif self.user_input == "2":
            self.level_hard()
        else:
            print("Invalid choice. Please enter 1 or 2")
            self.levels()

    def level_hard(self):
        """Hard level with the ability to play with the computer and the ability to choose the number of options."""
        self.load_results()
        while True:
            print(f"{self.name}, you need to choose options from the following: {', '.join(self.hard_level)}."
                  f"\nTo exit the game, enter !exit.\nTo see your rating, enter !rating.")
            option = input("Enter your choice: ")
            if option == "!rating":
                print(f"Your rating: {self.score}")
            elif option == "!exit":
                exit("Bye!")
            elif option != "!exit" or option != "!rating":
                option = option.split(",")
                for OPTION in option:
                    if OPTION.strip() in self.hard_level:
                        self.signs.append(OPTION.strip())
                if len(self.signs) == 0:
                    print("Error: Could not find options in the list")
                    continue
                elif len(self.signs) < 3:
                    print("Error: number of characters must be at least 3")
                    continue
                n = len(self.signs)
                self.winners = [[0 for _ in range(n)] for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        if i == j:
                            self.winners[i][j] = 0
                        elif (i == 0 and j == 1) or (i == 1 and j == 2) or (i == 2 and j == 0):
                            self.winners[i][j] = -1
                        else:
                            self.winners[i][j] = 1
            while True:
                user_input = input("Enter your choice: ")
                if user_input == "!rating":
                    print(f"Your rating: {self.score}")
                elif user_input == "!exit":
                    self.save_results()
                    exit("Bye!")
                elif user_input not in self.signs:
                    print("Error: This option is not in the list")
                    continue
                else:
                    self.pc_input = random.choice(self.signs)
                    i = self.signs.index(user_input)
                    j = self.signs.index(self.pc_input)
                    result = self.winners[i][j]
                    if result == 1:
                        print(f"Well done. The computer chose {self.pc_input} and failed")
                        self.score += 100
                    elif result == -1:
                        print(f"Sorry, but the computer chose {self.pc_input}")
                    else:
                        print(f"There is a draw ({self.pc_input})")
                        self.score += 50

    def level_easy(self):
        """Easy level with the ability to play with the computer."""
        self.load_results()
        print(f"{self.name}, you need to choose one of the following: rock, paper, scissors."
              f"\nTo exit the game, enter !exit.\nTo see your rating, enter !rating.")
        while True:
            self.pc_input = random.choice(self.easy_level)
            self.user_input = input("Enter your choice: ")
            if self.user_input == "!exit":
                self.save_results()
                exit("Bye!")
            elif self.user_input == "!rating":
                print(f"Your rating: {self.score}")
            elif self.user_input == self.pc_input:
                print(f"There is a draw ({self.pc_input})")
                self.score += 50
            elif self.user_input == "rock" and self.pc_input == "scissors":
                print(f"Well done. The computer chose {self.pc_input} and failed")
                self.score += 100
            elif self.user_input == "paper" and self.pc_input == "rock":
                print(f"Well done. The computer chose {self.pc_input} and failed")
                self.score += 100
            elif self.user_input == "scissors" and self.pc_input == "paper":
                print(f"Well done. The computer chose {self.pc_input} and failed")
                self.score += 100
            elif self.user_input == "rock" and self.pc_input == "paper":
                print(f"Sorry, but the computer chose {self.pc_input}")
            elif self.user_input == "paper" and self.pc_input == "scissors":
                print(f"Sorry, but the computer chose {self.pc_input}")
            elif self.user_input == "scissors" and self.pc_input == "rock":
                print(f"Sorry, but the computer chose {self.pc_input}")
            else:
                print("Invalid input. Please try again.")
                continue

    def menu(self):
        """Main menu of the game."""
        self.name = input("Enter your name: ")
        while True:
            print(f"Welcome {self.name} to Rock, Paper, Scissors!")
            print("1. Play Game")
            print("2. Rating")
            print("3. Exit Game")
            self.user_input = input("Enter your choice: ")
            if self.user_input == "1":
                self.levels()
            elif self.user_input == "2":
                self.show_results()
            elif self.user_input == "3":
                exit()
            else:
                print("Invalid choice. Please enter 1 or 2.")


# Main
if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.menu()
