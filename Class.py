# # Tools are used to interpret and they are programs
# # Python is an interpreted language
# # The online program is not a gui program, it is a console program
# # This is dynamically typed
# # Assignment operator works on right and left side
# # t=100
# # d=100
# # print()#No arguments
# # print("fdf")
# # print(t)
# # print("fdf")
# # print(d)
# # #
# # debug = 0
# # total_seconds = float(input("Enter"))
# # if debug:
# #     print(total_seconds)
# #     input()
# # hours = total_seconds // 3600
# # if debug:
# #     print(hours)
# #     input()
# # minutes = (total_seconds // 60) % 60
# # if debug:
# #     print(minutes)
# #     input()
# # seconds = total_seconds % 60
# # if debug:
# #     print(seconds)
# #     input()
# # print("Hours, minutes, seconds")
# # print("H", hours)
# # print("M", minutes)
# # print("S", seconds)
# #
# #
# #
# # future_value = float(input("Desire future value:"))
# # rate = float(input("Annual Interest rate:"))
# # years = int(input("Number of years the money will grow"))
# # present_value = future_value / (1.0 + rate)**years
# # print("need to deposit amount", present_value)
# #
# #
# # amount_due = 5000.0
# # monthly_payment = amount_due / 12.0
# # print(f"Monthly payment is {monthly_payment}.")
# # #
# #
# # name1 = "F"
# # name2 = "A"
# # name3= "B"
# # name4 = "C"
# # name5 = "D"
# # print(f"***{name1:^20}***")
# # print(f"***{name2:^20}***")
# # print(f"***{name3:^20}***")
# # print(f"***{name4:^20}***")
# # print(f"***{name5:^20}***")
# ##
# # high_score = 95
# # test1 = int(input("Enter the score for test1:"))
# # test2 = int(input("Enter the score for test2:"))
# # test3 = int(input("Enter the score for test3:"))
# # average = (test1 + test2 +test3) / 3.0
# # print(f"The average score is {average}")
# ##
# # base_hrs = 40
# # ot_multiplier = 1.5
# # hours = float(input("Enter number of hours worked"))
# # pay_rate = float(input("Enter the hourly pay rate"))
# # if hours > base_hrs:
# #     overtime_hrs = hours - base_hrs
# #     overtime_pay = overtime_hrs * pay_rate *ot_multiplier
# #     gross_pay = base_hrs * pay_rate *overtime_pay
# # else:
# #      gross_pay = hours * pay_rate
# # print(f"Gross pay is ${gross_pay:.2f}.")
# ##
# # pwd = input("Enter password")
# # if pwd == "prospero":
# #     print("password accepted")
# # else:
# #     print("Sorry, invalid password")
# ##
# # name1 = input("Enter a name (last name first):")
# # name2 = input("Enter another name (last name first):")
# # print("Here are the name, listed alphabetically.")
# # if name1 < name2:
# #     print(name1)
# #     print(name2)
# # else:
# #     print(name2)
# #     print(name1)
#
#
# no_of_sugar_cups=1.5
# no_of_butter_cups=1
# no_of_flour_cups=2.75
# no_of_cookies=48
# # taking the user input
# user_input_cookies = float(input('Number of cookies to be made: '))
# # mathematical caluculations
# sugar_required = (user_input_cookies*no_of_sugar_cups) / no_of_cookies
# butter_required = (user_input_cookies*no_of_butter_cups) / no_of_cookies
# flour_required = (user_input_cookies*no_of_flour_cups) / no_of_cookies
#
# # output the user can see
# print("We require "+str(round(sugar_required, 2)) + " cups of sugar, "+str(round(butter_required, 2)) + " cups of butter, "+str(round(flour_required, 2)) + " cups of flour.")
# #
#
no_of_male_students = int(input('Number of Male students in the class: '))
no_of_female_students = int(input('Number of Female students in the class: '))
# Mathematical caluculations
total_no_of_students = no_of_male_students + no_of_female_students
percentage_of_males = (no_of_male_students/total_no_of_students) * 100
percentage_of_females = (no_of_female_students/total_no_of_students) * 100
# Output user can see
print("Male student Percentage "+str(percentage_of_males))
print("Female student Percentage "+str(percentage_of_females))
#
#
# # stock_bought = 2000
# # amount_paid = 40.00
# # broker_share = 0.03
# # stock_sold = 2000
# # amount_got = 42.75
# # total_bought = stock_bought * amount_paid
# # total_got = stock_sold * amount_got
# # broker_bought = total_bought * broker_share
# # broker_got = total_got * broker_share
# # total = total_got - (total_bought + broker_got+broker_bought)
# # print("Joe paid "+str(total_bought+broker_bought)+" to buy the stock")
# # print("Joe paid "+str(broker_bought)+" to the broker")
# # print("Joe sold the stock for "+str(total_got + broker_got))
# # print("Joe payment "+str(broker_bought+broker_got)+" for broker in total")
# # print("Joe left with "+str(total))
# # if total > 0:
# #     print("Joe's profit")
# # else:
# #     print("Joe's loss")
