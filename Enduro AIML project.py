import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.\n")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret_number:
                print(f"That's it! You got it in {attempts} tries. The number was indeed {secret_number}.\n")
                return attempts
            elif abs(guess - secret_number) <= 10:
                if guess < secret_number:
                    print("A little low! You're close.")
                else:
                    print("A little high! You're close.")
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    high_score = float('inf')
    while True:
        print("--- Number Guessing Game Menu ---\n")
        print("1. Play a new game")
        print("2. View high score")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            current_attempts = play_game()
            if current_attempts < high_score:
                high_score = current_attempts
                print("You set a new high score!")
        elif choice == '2':
            if high_score == float('inf'):
                print("No games have been played yet.\n")
            else:
                print(f"Your best score (fewest attempts) is: {high_score}\n")
        elif choice == '3':
            print("Thanks for playing! Goodbye.\n")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

main()
