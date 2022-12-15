# Modules that will be used when exiting and restarting the program, as well as for using the collection
import collections
import sys
import os
# Collection that we will use in the future for some type of coffee
Consumption = collections.namedtuple("Consumption", "water, milk, coffee_beans, cups, money")


class CoffeeMachine:
    def __init__(self):
        # This is where the main resources of the coffee machine are stored.
        self.machine_standard_equipment = {
            "water": 400,
            "milk": 540,
            "coffee_beans": 120,
            "cups": 9,
            "money": 550
        }

    def fill(self):
        """Function to add resources to the coffee machine"""
        self.machine_standard_equipment['water'] += int(input("Write how many ml of water do you want to add: "))
        self.machine_standard_equipment['milk'] += int(input("Write how many ml of milk do you want to add: "))
        self.machine_standard_equipment['coffee_beans'] += int(input("Write how many grams of coffee "
                                                                     "beans do you want to add: "))
        self.machine_standard_equipment['cups'] += int(input("Write how many disposable cups of "
                                                             "coffee do you want to add: "))

    def take(self):
        """Function for issuing money"""
        print(f"I gave you {self.machine_standard_equipment['money']}$")
        self.machine_standard_equipment['money'] = 0

    def remaining(self):
        """A function to view the resources that are in the coffee machine, what is enough and what is not"""
        print("The coffee machine has:")
        print(f"{self.machine_standard_equipment['water']} of water")
        print(f"{self.machine_standard_equipment['milk']} of milk")
        print(f"{self.machine_standard_equipment['coffee_beans']} of coffee beans")
        print(f"{self.machine_standard_equipment['cups']} of cups")
        print(f"{self.machine_standard_equipment['money']} of money")

    def available_check(self, consumption):
        """Function for checking the availability of resources for preparing a particular type of coffee,
        if the result is positive, the resources are subtracted """
        if self.machine_standard_equipment['water'] - consumption.water < 0:
            print("Sorry, not enough water")
        elif self.machine_standard_equipment['milk'] - consumption.milk < 0:
            print("Sorry, not enough milk")
        elif self.machine_standard_equipment['coffee_beans'] - consumption.coffee_beans < 0:
            print("Sorry, not enough coffee beans")
        elif self.machine_standard_equipment['cups'] - consumption.cups < 0:
            print("Sorry, not enough cups")
        else:
            print("I have enough resources, making you a coffee!")
            self.machine_standard_equipment['water'] -= consumption.water
            self.machine_standard_equipment['milk'] -= consumption.milk
            self.machine_standard_equipment['coffee_beans'] -= consumption.coffee_beans
            self.machine_standard_equipment['cups'] -= consumption.cups
            self.machine_standard_equipment['money'] += consumption.money

    def buy(self):
        """The process of buying coffee"""
        buy_input = int(input("What do you want to buy? 1-espresso,2-latte,3-cappuccino,back to main menu:\n"))
        espresso = Consumption(250, 0, 16, 1, 4)
        latte = Consumption(water=350, milk=75, coffee_beans=20, cups=1, money=7)
        cappuccino = Consumption(water=200, milk=100, coffee_beans=12, cups=1, money=6)
        consumption = {1: espresso, 2: latte, 3: cappuccino}[buy_input]
        self.available_check(consumption)
        if buy_input == 'back':
            os.system("python coffeemachine.py")
            exit()

    def action(self):
        """Function by menu type with a choice of actions for the user"""
        if user_input == "buy":
            self.buy()
        elif user_input == "fill":
            self.fill()
        elif user_input == "take":
            self.take()
        elif user_input == "remaining":
            self.remaining()
        elif user_input == "exit":
            sys.exit("Goodbye!")
        else:
            print("Invalid Action")
        return True


# This is where our class starts.
machine = CoffeeMachine()
run = True
while run:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")
    run = machine.action()
