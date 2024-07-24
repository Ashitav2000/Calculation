"""
Given a list of numbers, return a list representing cumulative sum
Ex:
my_list = [100, 150, 300]
cum_sum_list = [100, 250, 550]
"""
def compute_cumulative_sum(my_list):
    sum_list=[]
    value = 0
    for num in my_list:
        value+= num
        sum_list.append(value)
    return sum_list

my_list = [350, 250, 100]
cum_sum = compute_cumulative_sum(my_list)
print(cum_sum)
assert cum_sum == [350, 600, 700]

