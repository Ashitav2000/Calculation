
"""
write a program that takes a list of strings and returns a dictionary with
keys representing the string and value representing the count


For ex:
my_list = ["a", "b", "a", "c", "a", "b", "c"]
value_counter(my_list)

{
"a": 3,
"b": 2,
"c": 2
}

"""


# def value_counter(my_list):
#     dic_count={}
#     for char in my_list:
#         if char in dic_count:
#             dic_count[char] += 1
#         else:
#             dic_count[char] = 1
#     return dic_count
#
#
# my_list = ["a", "b", "a", "c", "a", "b", "c"]
# value_counts_dict = value_counter(my_list)
# print(value_counts_dict)


"""
Write a function that takes in a list and returns True if there is
atleast one duplicate entry, otherwise return False

Ex 1: 
my_list = ["a", "b", "c", "a"]

has_duplilcates(my_list) # True

Ex 1: 
my_list = ["a", "b", "c"]

has_duplilcates(my_list) # False
"""

# def has_duplicates(my_list):
#     dup_count = {}
#     for char in my_list:
#         if char in dup_count:
#             dup_count[char] += 1
#             return True
#         else:
#             dup_count[char] = 1
#
#     return False

# def has_duplicates(my_list):
#     return len(set(my_list)) < len(my_list)
#
# my_list = ["a", "b", "c", "a"]
# print(has_duplicates(my_list))

# def predict_population(starting_population, daily_increase_percentage, days_to_multiply):
#     population = starting_population
#     result_table = []
#
#     for day in range(1, days_to_multiply + 1):
#         population *= (1 + daily_increase_percentage / 100)
#         result_table.append((day, population))
#
#     return result_table
#
# def display_population_table(data):
#     print("Day\tApproximate Population")
#     for day, population in data:
#         print(f"{day}\t{population:.5f}")
#
# # Get user input
# starting_population = float(input("Enter the starting number of organisms: "))
# daily_increase_percentage = float(input("Enter the average daily increase percentage: "))
# days_to_multiply = int(input("Enter the number of days to multiply: "))
#
# # Predict population
# population_data = predict_population(starting_population, daily_increase_percentage, days_to_multiply)
#
# # Display the table
# display_population_table(population_data)

def predict_population(starting, daily_increase, days):
    population = starting
    for day in range(1, days + 1):
        population *= 1 + daily_increase / 100
        print(f"Day {day}: {population:.5f}")

# Get user input
starting_population = float(input("Starting organisms: "))
daily_increase_percentage = float(input("Daily increase (%): "))
days_to_multiply = int(input("Days to multiply: "))

# Predict and display population
predict_population(starting_population, daily_increase_percentage, days_to_multiply)

