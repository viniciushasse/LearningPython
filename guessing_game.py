import random

print ("Let's play a guessing game, I will think of a number from 1 to 100 and you try to guess it, if the guess is wrong I'll give you a hint!")
number = random.randrange(1, 100)

for attempt in range(1, 11):
    guess = input(f"What's your guess? (attempt {attempt}/10) ")

    if guess == 'quit':
        print("Thanks for playing, see you next time!")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue

    if guess == number:
        print(f"Congratulations, your guess is right, the number is {number}") 
        break
    elif guess > number:
        print("Your guess is too high, try a lower one")
    else:
        print("Your guess is too low, try a higher number")

    if attempt == 10:
        print("Sorry, you have used up all your attempts.")
        break

print("Game over.")


