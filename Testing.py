# # nums=[2,7,11,15]
# # target=9
# # if nums[0]+nums[1]==target:
# #     print(nums[0:2])
# # elif nums[0]==nums[1]:
# #     print(nums[0],nums[1])
# # else:
# #     target=nums[0]+nums[1]
# #     print(nums[0:2])
# #     print(target)
#
# # Python program for implementation of Quicksort Sort
#
# # This implementation utilizes pivot as the last element in the nums list
# # It has a pointer to keep track of the elements smaller than the pivot
# # At the very end of partition() function, the pointer is swapped with the pivot
# # to come up with a "sorted" nums relative to the pivot
#
#
# # Function to find the partition position
# def partition(array, low, high):
#
# 	# choose the rightmost element as pivot
# 	pivot = array[high]
#
# 	# pointer for greater element
# 	i = low - 1
#
# 	# traverse through all elements
# 	# compare each element with pivot
# 	for j in range(low, high):
# 		if array[j] <= pivot:
#
# 			# If element smaller than pivot is found
# 			# swap it with the greater element pointed by i
# 			i = i + 1
#
# 			# Swapping element at i with element at j
# 			(array[i], array[j]) = (array[j], array[i])
#
# 	# Swap the pivot element with the greater element specified by i
# 	(array[i + 1], array[high]) = (array[high], array[i + 1])
#
# 	# Return the position from where partition is done
# 	return i + 1
#
# # function to perform quicksort
#
#
# def quickSort(array, low, high):
# 	if low < high:
#
# 		# Find pivot element such that
# 		# element smaller than pivot are on the left
# 		# element greater than pivot are on the right
# 		pi = partition(array, low, high)
#
# 		# Recursive call on the left of pivot
# 		quickSort(array, low, pi - 1)
#
# 		# Recursive call on the right of pivot
# 		quickSort(array, pi + 1, high)
#
#
# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)
#
# size = len(data)
#
# quickSort(data, 0, size - 1)
#
# print('Sorted Array in Ascending Order:')
# print(data)

def read_steps_file(steps):
    with open(steps, 'r') as file:
        steps_data = file.readlines()
    return [int(steps.strip()) for steps in steps_data]

def calculate_monthly_average(steps_data):
    monthly_averages = {}
    month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
                  'May': 31, 'June': 30, 'July': 31, 'August': 31,
                  'September': 30, 'October': 31, 'November': 30, 'December': 31}

    month_start = 0
    for month, days in month_days.items():
        month_steps = steps_data[month_start:month_start + days]
        monthly_averages[month] = sum(month_steps) / days
        month_start += days

    return monthly_averages

def write_average_to_file(averages):
    with open("Avg Steps.txt", 'w') as file:
        file.write("Month\t\tAverage Steps\n")
        for month, avg_steps in averages.items():
            file.write(f"{month}\t\t{avg_steps:.2f}\n")
        file.write("\nCreated by: Your Name")

def print_average_table(averages):
    print("Month\t\tAverage Steps")
    for month, avg_steps in averages.items():
        print(f"{month}\t\t{avg_steps:.2f}")

def main():
    steps_data = read_steps_file("steps.txt")
    monthly_averages = calculate_monthly_average(steps_data)
    write_average_to_file(monthly_averages)
    print_average_table(monthly_averages)

if __name__ == "__main__":
    main()
