# # Prompt the user to enter the name of the file
# filename = input("Enter the name of the file: ")
# try:
#     # Try to open the specified file in read mode
#     with open(filename) as f:
#         # Reading all lines from the file into a list
#         lines = f.readlines()
#         for i, line in enumerate(lines, start=1):
#             print(f"{i}: {line}", end="")
# # Handle the FileNotFoundError in case the specified file is not found
# except FileNotFoundError:
#     print(f"Error: file '{filename}' not found.")

# # Specify the name of the file to be processed
# filename = "names.txt"
# # Initialize a variable to count the number of names in the file
# count = 0
# # Open the file in read mode using a with statement
# with open(filename) as f:
#     for line in f:
#         count += 1
# # Print the result
# print(f"The file '{filename}' contains {count} names.")

# # Initialize a variable
# total = 0
# # Opening the file "numbers.txt" in read mode using a with statement
# with open("numbers.txt", "r") as file:
#     # Iterate over each line in the file
#     for line in file:
#         try:
#             # convert the current line to an integer and strip any leading/trailing whitespace
#             num = int(line.strip())
#             total += num
#         except ValueError:
#             # Handle the case where the line does not represent a valid integer
#             print(f"Skipping non-integer value: {line.strip()}")
# # Print the final result
# print(f"The sum of all numbers in the file is: {total}")


# # Initialize variables to store the total sum and count of numbers
# total = 0
# count = 0
# # Open the file "numbers.txt"
# with open("numbers.txt", "r") as file:
#     for line in file:
#         try:
#             # convert the current line to an integer and strip any leading/trailing whitespace
#             num = int(line.strip())
#             total += num
#             count += 1
#         except ValueError:
#             print(f"Skipping non-integer value: {line.strip()}")
# # Check if there are valid numbers in the file
# if count > 0:
#     # Calculate the average of the valid numbers
#     average = total / count
#     # Print the result
#     print(f"The average of all numbers in the file is: {average}")
# else:
#     # Print a message stating that no valid numbers were found in the file
#     print("No valid numbers found in the file.")


# # Import the random module to generate random numbers
# import random
# # user to input the number of random numbers to generate
# num_numbers = int(input("How many random numbers do you want to generate? "))
# # Open the file "random_numbers.txt"
# with open("random_numbers.txt", "w") as file:
#     for i in range(num_numbers):
#         num = random.randint(1, 500)
#         # Writing the random number to the file
#         file.write(str(num) + "\n")
# # Print a message stating the successful generation
# print(f"{num_numbers} random numbers have been written to the file 'random_numbers.txt'.")


# # Import the random module to generate random numbers
# import random
# try:
#     # User to input the number of random numbers to generate
#     num_numbers = int(input("How many random numbers do you want to generate? "))
#     # Open the file "random_numbers.txt"
#     with open("random_numbers.txt", "w") as file:
#         for i in range(num_numbers):
#             num = random.randint(1, 500)
#             file.write(str(num) + "\n")
#     # Print a message stating the successful generation
#     print(f"{num_numbers} random numbers have been written to the file 'random_numbers.txt'.")
# # Handle IOError, that are raised when the file is opened, and data is
# # read from it.
# except IOError:
#     print("Error: Could not write to file.")
# # Handle ValueError and TypeError,
# # that are raised when the items that are read from the  file  are  converted  to  a  number.
# except (ValueError, TypeError):
#     print("Error: Invalid input. Please enter a valid integer for the number of random numbers to generate.")


# # Open the file 'golf.txt'
# with open('golf.txt', 'w') as file:
#     # Use a loop to continuously input player names and scores until 'q' is entered
#     while True:
#         # User to enter the player's name (or 'q' to quit)
#         name = input("Enter the player's name (or 'q' to quit): ")
#         if name.lower() == 'q':
#             break
#         # User to enter the player's golf score
#         score = input("Enter the player's golf score: ")
#         # Write the player's name and score to the file
#         file.write(f"{name},{score}\n")
# # Print a message
# print("Golf scores written to 'golf.txt'.")


# # Open the file 'golf.txt'
# with open('golf.txt', 'r') as file:
#     # Print header for the table displaying Player Name and Golf Score
#     print("Player Name\tGolf Score")
#     for line in file:
#         # Splitting each line into the player's name and golf score
#         name, score = line.strip().split(',')
#         # Print the player's name and golf score
#         print(f"{name}\t\t{score}")
