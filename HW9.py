# 1 # created a function to print numbers from n to 1 recursively
# def print_numbers(value):
#     if value == 1:
#         print(value)
#     else:
#         # print numbers from value-1 down to 1
#         print_numbers(value-1)
#         # Print the current value of n
#         print(value)
#
#
# try:
#     # get user input for n
#     n = int(input("Enter an integer: "))
#     # Checking if the input is non-positive
#     if n <= 0:
#         print("Enter a positive integer")
#     else:
#         # Calling the print_numbers function
#         print_numbers(n)
# except ValueError:
#     # print the error message when user enters a non-integer input
#     print("Invalid input. Please enter an integer.")


# 2 # Created a function to perform multiplication recursively
# def recursive_multiply(a, b):
#     # when b is 1, return a
#     if b == 1:
#         return a
#     else:
#         # return a plus the result of multiplying a by b-1
#         return a + recursive_multiply(a, b - 1)
#
#
# try:
#     # get user input for x and y
#     x = int(input("Enter a positive integer for x: "))
#     y = int(input("Enter a positive integer for y: "))
#
#     if x <= 0 or y <= 0:
#         print("Enter a positive integer")
#     else:
#         result = recursive_multiply(x, y)
#         # Print the result of the multiplication
#         print(f"{x} times {y} is {result}")
# except ValueError:
#     # print the error message when user enters a non-integer input
#     print("Invalid input. Please enter an integer.")


# def asterisk_lines(value):
#     # Check if the value is a positive integer
#     if value <= 0:
#         # Print an error message if the value is not a positive integer
#         print("Please enter a positive integer")
#         return
#
#     # display one asterisk
#     if value == 1:
#         print("*")
#     # display value-1 lines of asterisks, then display the result
#     else:
#         asterisk_lines(value - 1)  # calling asterisk_lines function
#         print("*" * value)  # Print the result
#
#
# try:
#     # input the value
#     input_value = int(input("Enter a positive integer: "))
#     # Call the asterisk_lines function
#     asterisk_lines(input_value)
# except ValueError:
#     # print the error message when user enters a non-integer input
#     print("Please enter a valid integer.")

# 4 # Created a function to find the largest item in a list recursively
# def largest_item(input_list):
#     # If the list has only one item, return that item
#     if len(input_list) == 1:
#         return input_list[0]
#     else:
#         # largest item in the list starting from index 1
#         list_max = largest_item(input_list[1:])
#         # Return the first item of the current list if it's greater than the largest item in the sublist,
#         # otherwise return the largest item in the sublist
#         return input_list[0] if input_list[0] > list_max else list_max
#
#
# # Define a list of integers
# numbers_list = [15, 20, 5, 30, 4, 7, 1]
# # print the result by calling the largest_item function
# print(largest_item(numbers_list))  # Output: 30

# # 5
# def list_sum(list_value):
#     # if the list_value has only one element, return that element
#     if len(list_value) == 1:
#         return list_value[0]
#     else:
#         return list_value[0] + list_sum(list_value[1:])
#
#
# # creating a list of integers
# list_numbers = [4, 1, 5, 7, 10]
# # Call the list_sum function and print the result
# print(list_sum(list_numbers))  # Output: 27


# 6
# Creating a function for accepting integer argument
def sum_of_numbers(value):
    # value is less than 1, return an error message
    if value < 1:
        return "Please enter a positive integer"
    # value is 1, return 1
    elif value == 1:
        return 1
    else:
        return value + sum_of_numbers(value - 1)


try:
    # enter the user input for n
    n = int(input("Enter an integer: "))
    # if n is non-positive
    if n <= 0:
        print("Enter a Positive Integer")
    else:
        # Call the sum_of_numbers function and print the result
        print(sum_of_numbers(n))
except ValueError:
    # print the error message when user enters a non-integer input
    print("Invalid input. Please enter an integer.")


# 7
# # creating a function
# def power(b, expo):
#     # if expo is 0, return 1
#     if expo == 0:
#         return 1
#     # if the expo is 1, return the b
#     elif expo == 1:
#         return b
#     else:
#         return b * power(b, expo - 1)
#
#
# # enter the input for the base_value and the exponent_value
# base_value = float(input("Enter the base number: "))
# exponent_value = int(input("Enter the exponent (a non-negative integer): "))
#
# if exponent_value < 0:
#     print("Exponent must be a non-negative integer.")
# else:
#     # Calculate the output using the power function and print it
#     output = power(base_value, exponent_value)
#     print(f"{base_value} raised to the power of {exponent_value} is: {output}")
