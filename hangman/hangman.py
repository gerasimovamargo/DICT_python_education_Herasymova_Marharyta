import random
import sys

words = ('python', 'java', 'javascript', 'php')
our_mistakes = 0
max_mistakes = 8
random_word = random.choice(words)


def menu():
    print("[CHOOSE A NUMBER]")
    print("[1] START!")
    print("[2] EXIT")


def cycle():
    global our_mistakes
    length = '_' * len(random_word)
    used_letters = []
    print("HANGMAN""\nThe game will be available soon.")

    while our_mistakes < max_mistakes and length != random_word:

        print("\n You used this letter >\n", used_letters)
        print("\n At the moment the word looks like this >\n", length)

        print("\n EXIT GAME - WRITE \"Exit\"")
        letter = input("\n Please enter above guess > ")

        if letter in used_letters:
            print("You already guessed that letter!", letter)
            continue
        if letter == "Exit":
            sys.exit("Goodbye!")
        elif len(letter) > 1:
            print("\n You must enter one letter.Try again")
        elif letter == letter.upper():
            print("\n Turn capslock off or don't use numbers!")

        used_letters.append(letter)
        if letter in random_word:
            print("Great! \'" + letter + "\" is in the word")

            new = ''
            for x in range(len(random_word)):
                if letter == random_word[x]:
                    new += letter
                else:
                    new += length[x]
            length = new
        else:
            print("\n Sorry, no letter \"" + letter + "\" in the word")
            our_mistakes += 1
            print("Your mistakes - >", our_mistakes)


def win_or_not():
    if our_mistakes == max_mistakes:
        print("\nYou lost!")

    else:
        print("\nYou survived!")

    print("The hidden word was \"" + random_word + "\" ")


menu()
player = int(input("Enter your choice:"))
while player != 0:
    if player == 1:
        cycle()
        win_or_not()
        pass
    elif player == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print("Invalid Choice!")
    print()
    menu()
    player = int(input("Enter your choice:"))
