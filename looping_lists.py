# iterating through lists
my_list = [100, 101, 102, 103]
length = len(my_list)

# for i in range(length):
#     print(my_list[i])

# for number in my_list:
#     print(number)

# my_list_2 = [100, 101, 102, 103, 104, 105]
# print("before loop", my_list_2)
# for i in range(len(my_list_2)):
#     my_list_2[i] = my_list_2[i] + 1
# print("after loop ", my_list_2)
#

my_list = [199, 1209, 121, 13711, 11, 200, 700, 900]

# def extract_even_numbers_from_list(some_list_variable):
#     even_numbers_list = []
#     for i in range(len(some_list_variable)):
#         if some_list_variable[i] % 2 == 0:
#             even_number = some_list_variable[i]
#             even_numbers_list.append(even_number)
#
#     return even_numbers_list
#
#
# my_even_numbers = extract_even_numbers_from_list(my_list)
# print(my_even_numbers)


# def is_even_number(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def extract_odd_numbers_from_list(some_list_variable):
#     odd_numbers_list = []
#     for i in range(len(some_list_variable)):
#         if not is_even_number(some_list_variable[i]):
#             odd_number = some_list_variable[i]
#             odd_numbers_list.append(odd_number)
#
#     return odd_numbers_list
#
#
# my_odd_numbers = extract_odd_numbers_from_list(my_list)
# print(my_odd_numbers)
#
#

def compute_sum_of_numbers(nums_list):
    total_sum=0
    for num in nums_list:
        total_sum += num
    return total_sum
def compute_average_marks(marks_list):
    total_sum = compute_sum_of_numbers(marks_list)
    return total_sum/len(marks_list)
student_marks = [70,80,90]
average = compute_average_marks(student_marks)
print(f"The Average of 70, 80 and 90 = {average}")