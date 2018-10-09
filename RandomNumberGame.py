import random
number = random.randint(1, 100)

name = input("Hi whats your name?")
print ("Well, ", name, "i am thinking of a number between 1 and 100 can you guess it?")

guess = int(input())

while (guess != number):
    if (guess > number):
        print("Your guess is way too high.")
    else:
        print("Your guess is way too low.")
    guess = int(input())

if (guess == number):
    print("Correct!")
