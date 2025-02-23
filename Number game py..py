import random


# Function to play the number guessing game
def play_game():
    print("Welcome to the Number Guessing Game!")

# Random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
# Get user's guess
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
    play_game()


    '''How to play the game:
1.The program generates a random number between 1 and 100.
2.The player guesses the number, and the program provides feedback:
"Too low!" if the guess is less than the number.
"Too high!" if the guess is more than the number.
"Congratulations!" if the guess is correct.
3.The game counts how many attempts the player made.'''