import sys
import random


def count(users_num, our_users, total_amount):
    total_amount /= users_num
    friendly_company = dict.fromkeys(our_users, round(total_amount, 2))
    print(friendly_company)


def yes_choice(our_users, total_amount, users_num):
    happy = random.choice(our_users)
    print(happy + " is the lucky one! ")
    new_price = total_amount / (users_num - 1)
    friendly_company = dict.fromkeys(our_users, new_price)
    friendly_company[happy] = 0
    print(friendly_company)
    print("Thank you for using our program!")


def check(our_users, users_num):
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(users_num):
        our_users.append(str(input("-> ")))
    print("Friends:")
    for i in range(len(our_users)):
        print("|-" + our_users[i] + "-|")
    friendly_company = dict.fromkeys(our_users, 0)
    print(friendly_company)


def luck_choice():
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    print("[YES]")
    print("[NO]")


def luck_process(user_choice, our_users, total_amount, users_num):
    while user_choice != "Exit":
        if user_choice == "YES":
            yes_choice(our_users, total_amount, users_num)
            sys.exit("Goodbye!")
            pass
        elif user_choice == "NO":
            print("No one is going to be lucky :(")
            print("Thank you for using our program!")
            count(users_num, our_users, total_amount)
            sys.exit("Goodbye!")
            pass
        else:
            print("Invalid Choice!")

        luck_choice()
        user_choice = input("Enter your choice:")


def process():
    users_num = 0
    while users_num != "users_num":
        our_users = []
        print("Enter the number of friends joining (including you)")
        users_num = int(input("-> "))
        if users_num <= 0:
            print("No one is joining for the party")
            continue
        check(our_users, users_num)
        total_amount = int(input("-> "))
        count(users_num, our_users, total_amount)
        luck_choice()
        user_choice = input("Enter your choice:")
        luck_process(user_choice, our_users, total_amount, users_num)


def menu():
    print("SHARING OF COMMON COSTS")
    print("[1] ENTER PARTICIPANTS!")
    print("[2] EXIT")


menu()
user = int(input("Enter your choice:"))
while user != 0:
    if user == 1:
        process()
        pass
    elif user == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print("Invalid Choice!")

    menu()
    user = int(input("Enter your choice:"))
