import random as ran

guesses_taken = 0

print("Hello, what is your name?")

name = input()

number = ran.randint(1, 20)

print("So, " + name + ", I am thinking a number.")

for guesses_taken in range(6):
    
    print("Let's guess it.")
    
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is less then number.")

    if guess > number:
        print("Your guess is bigger then number")

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print("Well done! You did it in " + guesses_taken + " attemps.")

if guess != number:
    number = str(number)
    print("Unfortunatly, yo did not do it. A number was " + guesses_taken + ".")

