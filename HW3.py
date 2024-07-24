# # 1
# number = int(input("Enter the number in the range of 1 through 7: "))
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("Error: The number is not within the range of 1 through 7!")
# # 2
# length_1 = int(input("Enter the length of first rectangle-1: "))
# width_1 = int(input("Enter the width of rectangle-1: "))
# length_2 = int(input("Enter the length of first rectangle-2: "))
# width_2 = int(input("Enter the width of rectangle-2: "))
# area_1 = (length_1 * width_1)
# area_2 = (length_2 * width_2)
# if area_1 > area_2:
#     print("Area of rectangle-1 is greater than rectangle-2")
# elif area_1 < area_2:
#     print("Area of rectangle-2 is greater than rectangle-1")
# else:
#     print("The area of both the rectangles are same")
# # 3
# age = int(input("Enter the age: "))
# if age <= 1:
#     print("She is an infant")
# elif 1 < age < 13:
#     print("You are a child")
# elif 13 <= age < 20:
#     print("You are a teenager")
# elif age >= 20:
#     print("You are an adult")
# # 4
# number_numerals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
# input_number = int(input("Enter the number within the range of 1 through 10: "))
# if input_number == 1:
#     print(f"Roman numeral of 1: {number_numerals[1]}")
# elif input_number == 2:
#     print(f"Roman numeral of 2: {number_numerals[2]}")
# elif input_number == 3:
#     print(f"Roman numeral of 3: {number_numerals[3]}")
# elif input_number == 4:
#     print(f"Roman numeral of 4: {number_numerals[4]}")
# elif input_number == 5:
#     print(f"Roman numeral of 5: {number_numerals[5]}")
# elif input_number == 6:
#     print(f"Roman numeral of 6: {number_numerals[6]}")
# elif input_number == 7:
#     print(f"Roman numeral of 7: {number_numerals[7]}")
# elif input_number == 8:
#     print(f"Roman numeral of 8: {number_numerals[8]}")
# elif input_number == 9:
#     print(f"Roman numeral of 9: {number_numerals[9]}")
# elif input_number == 10:
#     print(f"Roman numeral of 10: {number_numerals[10]}")
# else:
#     print("Error: The number entered is not within the range of 1 through 10!")
# # 5
# object_mass = int(input("Enter the mass value of an object: "))
# object_weight = object_mass * 9.8
# if object_weight > 500:
#     print("The object is too heavy")
# elif object_weight < 100:
#     print("The object is too light")
# # 6
# month = int(input("Enter the month: "))
# day = int(input("Enter the day: "))
# year = int(input("Enter the year: "))
# if month * day == year:
#     print ("The date is magic")
# else:
#     print ("The date is not magic")
# # 7
# color_1 = input("Enter the first primary colour: ")
# color_2 = input("Enter the second primary colour: ")
# if (color_1 == "red" and color_2 == "blue"):
#     print("The Secondary colour is: Purple")
# elif (color_1 == "red" and color_2 == "yellow"):
#     print("The secondary Colour is: Orange")
# elif (color_1 == "blue" and color_2 == "yellow"):
#     print("The Secondary colour is: Green")
# else:
#     print("Error: You have entered wrong colours! Please enter red or blue or yellow")
# # 8
# people_count = int(input("Enter the number of people attending the cookout: "))
# hotdogs_per_person = int(input("Enter the number of hot dogs per person: "))
# total_hotdogs = people_count * hotdogs_per_person
# hotdog_packages = total_hotdogs // 10
# hotdogs_leftover = total_hotdogs % 10
# total_hotdog_buns = people_count * hotdogs_per_person
# hotdog_bun_packages = total_hotdog_buns // 8
# hotdog_buns_leftover = total_hotdog_buns % 8
# print("Minimum number of packages of hot dogs required:", hotdog_packages)
# print("Minimum number of packages of hot dog buns required:",hotdog_bun_packages)
# print("Number of hot dogs that will be left over:", hotdogs_leftover)
# print("Number of hot dog buns that will be left over:", hotdog_buns_leftover)
# # 9
# pocket_number = int(input("Enter a pocket number"))
# if pocket_number == 0:
#     print("Green")
# elif pocket_number >=1 and pocket_number <=10:
#     if pocket_number % 2 ==0:
#         print("Black")
#     else:
#         print("Red")
# elif pocket_number >= 11  and pocket_number <= 18:
#     if pocket_number % 2 == 0:
#         print("Red")
#     else:
#         print("Black")
# elif pocket_number >= 19 and pocket_number <= 28:
#     if pocket_number % 2 == 0:
#         print("Black")
#     else:
#         print("Red")
# elif pocket_number >= 29 and pocket_number <= 36:
#     if pocket_number % 2 == 0:
#         print("Red")
#     else:
#         print("Black")
# else:
#     print("Error: Enter the pocket number in range of 0 to 36!")
#
#taking the user input
ck = int(input("Number of cookies the user want to made: "))

#mathematical caluculations
receipe_produced_cookies = 48
number_of_cups_of_suger = ((ck*1.5)/receipe_produced_cookies)
number_of_cups_of_butter = ((ck*1)/receipe_produced_cookies)
number_of_cups_of_floor = ((ck*2.75)/receipe_produced_cookies)

#output the user can see
print("Number of cups of Sugar needed: ",number_of_cups_of_suger)
print("Number of cups of Butter needed: ",number_of_cups_of_butter)
print("Number of cups of Floor needed: ",number_of_cups_of_floor)