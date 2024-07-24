# # 1
# # total_bugs = 0
# # for day in range(1, 6):
# #     bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
# #     total_bugs += bugs_collected
# # print(f"\nTotal number of bugs collected in five days: {total_bugs}")
#
# # 2
# # calories_per_min = 4.2
# # for mins in [10, 15, 20, 25, 30]:
# #     calories_burnt = mins * calories_per_min
# #     print(f"After {mins} minutes, you've burned {calories_burnt} calories.")
#
# # 3
# # budget_amount = float(input("Enter the amount that was budgeted for the month: "))
# # total_expenses = 0
# # while True:
# #     expense_month = float(input("Enter each expense for a month: "))
# #     if expense_month == 0:
# #         break
# #     total_expenses += expense_month
# # over_under_budget = total_expenses - budget_amount
# # if over_under_budget < 0:
# #     print(f"You are under budget by {over_under_budget}.")
# # elif over_under_budget > 0:
# #     print(f"You are over budget by {over_under_budget}.")
# # else:
# #     print("You have exactly met your budget.")
#
# # 4
# # input_value = int(input("Enter a number: "))
# # fac = 1
# # i = 1
# # while i <= input_value:
# #     fac = fac * i
# #     i = i + 1
# # print(f"Factorial of {input_value} is {fac}")
#
# # 5

# starting_population = float(input("Enter the organism population in the beginning: "))
# daily_increase_percentage = float(input("Enter the increase in population: "))
# total_noOf_days = int(input("Enter the total number of days: "))
# # Predict and display population
# population = starting_population
# print("Day\tApproximate Population")
#
# # Calculate and print population for each day
# for day in range(1, total_noOf_days + 1):
#     print(f"{day}\t{population:.5f}")
#     population *= (1 + daily_increase_percentage / 100)

# # 6
# # for i in range(7, 0, -1):
# #     for j in range(i):
# #         print('*', end=' ')
# #     print()
# # OR
# i=7
# while i>0:
#     j = 0
#     while j < i:
#         print('*', end=' ')
#         j += 1
#     print()
#     i -= 1
#
# # 7
i = 1
while i < 7:
    j = 0
    while j <= i:
        if j == 0 or j == i:
            print("#", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
