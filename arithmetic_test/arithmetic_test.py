"""Arithmetic Test Program"""

# Libraries
import sys
import random
import os
import json


class ArithmeticTest:
    def __init__(self):
        """Initialize the class attributes"""
        self.x = None
        self.y = None
        self.z = None
        self.operator = None
        self.correct_answers = None
        self.score = 0
        self.answer = None
        self.max_questions = 5
        self.name = ""

    def save_results(self):
        """Save the results to a file in JSON format. If the file does not exist, create it."""
        if not os.path.exists("results.txt"):
            with open("results.txt", "w") as f:
                json.dump({}, f)

        with open("results.txt", "r") as f:
            results = json.load(f)

        name = self.name
        score = self.score
        attempt = len(results.get(name, [])) + 1

        if name not in results:
            results[name] = []
        results[name].append({"attempt": attempt, "score": score})

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
            print(f"Attempt {result['attempt']}: {result['score']}")

    def menu(self):
        """Display the menu and call the appropriate function depending on the user's choice."""
        print("Welcome to the Arithmetic Test")
        while True:
            print("[1]Simple Operations with numbers 2-9")
            print("[2]Integral squares from 11 to 29")
            print("[3]Check results")
            print("[4]Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.simple_operations()
            elif choice == "2":
                self.integral_squares()
            elif choice == "3":
                self.name = input("Enter your name, please:")
                self.show_results()
            elif choice == "4":
                sys.exit("Goodbye!")
            else:
                print("Wrong choice!")

    def simple_operators(self):
        """Generate random numbers and operators. Calculate the correct answer."""
        self.x = random.randint(2, 9)
        self.y = random.randint(2, 9)
        self.operator = random.choice(['+', '-', '*'])
        if self.operator == '+':
            self.correct_answers = self.x + self.y
        elif self.operator == '-':
            self.correct_answers = self.x - self.y
        else:
            self.correct_answers = self.x * self.y

    def simple_operations(self):
        """
        Ask the user to enter the correct answer to the expression.
        Check the user's answer and then display the result.
        At the end of the game, ask the user if he wants to save the result.
        """
        for i in range(self.max_questions):
            print(f"Question {i + 1}:")
            self.simple_operators()
            self.answer = input(f"What is the result of the expression {self.x} {self.operator} {self.y}?\n=>")
            while True:
                try:
                    if int(self.answer) == self.correct_answers:
                        self.score += 1
                        print("Correct!")
                        break
                    else:
                        print("Incorrect! The correct answer is", self.correct_answers)
                        break
                except ValueError:
                    print("Invalid input, please enter a number!")
                    self.answer = input(f"What is the result of the expression {self.x} {self.operator} {self.y}?\n=>")
        user_input = input(f"Your score is {self.score}, out of {self.max_questions} questions asked!"
                           f"\nWould you like to save your score? (y/n)\n=>")
        while True:
            if user_input in ["y", "yes", "Yes", "YES", "Y"]:
                self.name = input("Enter your name, please:")
                self.save_results()
                sys.exit("Thank you for playing!")
            elif user_input in ["n", "no", "No", "NO", "N"]:
                self.menu()
            else:
                print("Wrong choice!")
                user_input = input("Would you like to save your score? (y/n)\n=>")

    def integral_squares(self):
        """
        Integral squares from 11 to 29.
        Ask the user to enter the correct answer.
        Check the user's answer and then display the result.
        At the end of the game, ask the user if he wants to save the result.
        """
        for i in range(self.max_questions):
            self.z = random.randint(11, 29)
            self.correct_answers = self.z ** 2
            self.answer = input(f"What is the square of the number {self.z}?\n=>")
            while True:
                try:
                    if int(self.answer) == self.correct_answers:
                        self.score += 1
                        print("Correct!")
                        break
                    else:
                        print("Incorrect! The correct answer is", self.correct_answers)
                        break
                except ValueError:
                    print("Invalid input, please enter a number!")
                    self.answer = input(f"What is the square of the number {self.z}?\n=>")
        user_input = input(f"Your score is {self.score}, out of {self.max_questions} questions asked!"
                           f"\nWould you like to save your score? (y/n)\n=>")
        while True:
            if user_input in ["y", "yes", "Yes", "YES", "Y"]:
                self.name = input("Enter your name, please:")
                self.save_results()
                sys.exit("Thank you for playing!")
            elif user_input in ["n", "no", "No", "NO", "N"]:
                self.menu()
            else:
                print("Wrong choice!")
                user_input = input("Would you like to save your score? (y/n)\n=>")


# Main
if __name__ == "__main__":
    a = ArithmeticTest()
    a.menu()
