import random


def guess_the_number():
    number = random.randint(1, 100)
    counter = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        counter += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {counter} attempts.")
            break


guess_the_number()
