import random

def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0  # Track the number of attempts

    print("Welcome to 'Guess the Number'!")
    print("I've picked a number between 1 and 100. Can you guess it?")

    # Start the guessing loop
    while True:
        try:
            # Ask the player to enter their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempt count

            # Check if the guess is too low, too high, or correct
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break  # End the loop if guessed correctly
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_the_number()
