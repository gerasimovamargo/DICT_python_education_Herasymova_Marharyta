print("Hello! My name is DICT_Bot")
print("I was created in 2020")

print("Please, remind me your name")
user_input = input(">")
print("What a great name you have,", user_input, '!')

print("Let me guess your age")
print("Enter remainders of dividing your age by 3, 5 and 7")
remainder3 = input(">")
remainder5 = input(">")
remainder7 = input(">")
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is" ,age,",that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want")
from_num = (int)(input(">"))
print("Counting numbers from " + str(from_num))
for number in range (from_num + 1):
    print(number, "!")
print("Completed, have a nice day!")

print("1.To repeat a statement multiple times.""\n2.To decompose a program into several small subroutines.""\n3.To determine the execution time of a program.""\n4.To interrupt the execution of a program.")
y = 0
while y != 2:
    y = int(input("Try to guess the answer:"))
    if (y > 2):
        print("Please, try again!")
    if (y < 2):
        print("Please, try again!")
    if (y == 2):
        print("Completed, have a nice day!""\nCongratulations, have a nice day!")

