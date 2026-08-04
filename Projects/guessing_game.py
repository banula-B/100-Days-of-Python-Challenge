# This is a number guessing game

secret_number = 7


user_guess = int(input("Guess the secret number (1-10): "))
    
if user_guess == secret_number:
    print("Correct! You guessed the number.")
    
elif user_guess < secret_number:
    print("Too low! Try a larger number next time.")
else:
    print("Too high! Try a smaller number next time.")
        