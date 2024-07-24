s1={'n':'R', 'g':'M'}
# print(s1)
# s2={'n':'R', 'g':['M','A']}
print("A\nB\nC\nD\nE\nF")
name = "Ashita Vemulapalli"
study_major = "Cyber Security and Networks"
college_name = "University of New Haven"
graduation_year = "2025"
print("1. " + name)
print("2. " + study_major)
print("3. " + college_name)
print("4. " + graduation_year)
def sum_of_numbers(nums_list):
    total=0
    for num in nums_list:
        total += num
    return total
def average_of_numbers(total_list):
    total = sum_of_numbers(total_list)
    return total/len(total_list)
numbers = [70,80,90]
average = average_of_numbers(numbers)
print(f"The Average of 70, 80 and 90 = {average}")
# print(s2)
# print(s2['g'])
# print(s1.get('p'))
# print(s1.get('p','not found'))
# s1['p']='44'
# print(s1.get('p','not found'))
# s1.update({'n':'T', 'g':'F','p':'2244' })
# print(s1)
# #del s1['n']
# #print(s1)
# g=s1.pop('g')
# print(g)
# print(s1.values())
# print(s1.items())
for key, value in s1.items():
    print(value)

