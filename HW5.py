# # 1
# # Import the random module to generate random numbers
# import random
# # Initialize counters for even and odd numbers
# even_count = 0
# odd_count = 0
# # Generate 100 random numbers and count even and odd numbers
# for _ in range(100):
#     num = random.randint(1, 100)
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# # Print the results
# print("The 100 random numbers are generated.")
# print("Even numbers count:", even_count)
# print("Odd numbers count:", odd_count)
#
# # 2
# def is_prime(number):
#     # Return True if the given number is prime, else False
#     if number < 2:
#         return False  # Numbers less than 2 are not prime
#     for value in range(2, int(number**0.5) + 1):
#         if number % value == 0:
#             return False  # If the number is divisible by any integer in the range, it's not prime
#     return True  # If no divisor is found, the number is prime
#
# # Prompt user to enter a number
# user_input = int(input("Enter a number: "))
# # Check whether the entered number is prime or not
# if is_prime(user_input):
#     print(f"{user_input} is a prime number.")
# else:
#     print(f"{user_input} is not a prime number.")
#
# # 3
# # Define a function to check if a given value is a prime number
# def is_prime(value):
#     # Numbers less than 2 are not prime
#     if value < 2:
#         return False
#     # Check for factors from 2 to the square root of the value
#     for i in range(2, int(value ** 0.5) + 1):
#         # If the value is divisible by i, it is not prime
#         if value % i == 0:
#             return False
#     return True
# print("Prime numbers from 1 to 100:")
# # Looping the numbers from 1 to 100 and check if they are prime or not
# for i in range(1, 101):
#     if is_prime(i):
#         print(i, end=' ')
#
# # 4
# # Define a function to calculate the future value using compound interest formula
# def calculate_future_value(present_value, monthly_interest, number_of_months):
#     """Calculate the future value of a savings account."""
#     future_value = present_value * (1 + monthly_interest)**number_of_months
#     return future_value
# # Prompt user to enter account information
# present_value = float(input("Enter the present balance of the account: "))
# monthly_interest = float(input("Enter monthly interest rate (as a decimal): "))
# number_of_months = int(input("Enter the number of months the money will be left in the account: "))
# # Calculate and display the future value of the account
# future_value = calculate_future_value(present_value, monthly_interest, number_of_months)
# print(f"The future value of the account after {number_of_months} months is ${future_value:.2f}")


# 5
# Using Import random to generate a random number
import random
def guess_the_number():
    # Generate a new random number and reset guess value
    number = random.randint(1, 100)
    # Initialize the number of guess_number_count
    guess_number_count = 0
    # Start an infinite loop for the guessing game
    while True:
        # Get user input for the guess
        user_guess = int(input("Guess the number (1-100): "))
        guess_number_count += 1
        # Check if the user's guess is correct, too high, or too low
        if user_guess == number:
            print(f"Congratulations! You guessed the number in {guess_number_count} guess_number_count.")
            break
        elif user_guess > number:
            print("Too high, try again.")
        else:
            print("Too low, try again.")
# Call the guessing game function
guess_the_number()
