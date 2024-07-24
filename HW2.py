# annual_profit = 23
# projected_amount_of_sales = float(input("Enter the amount of total sales: "))
# print("Profit: ", projected_amount_of_sales*0.23)
#
# one_acre_Sqrfeet = 43560
# total_sqrfeet = float(input("Enter the total square feet in a tract of land: "))
# number_of_acres = total_sqrfeet / one_acre_Sqrfeet
# print(f"The number of acres in the tract is {number_of_acres}")
#
# sales_tax = 0.07
# sub_total = 0.0
# for i in range(1, 6):
#     each_item_price = float(input(f"Enter the price for item {i}: $ "))
#     sub_total += each_item_price
# sales_tax_total = sub_total * sales_tax
# total = sub_total + sales_tax_total
# print(f"Subtotal: ${sub_total}")
# print(f"Sales Tax: ${sales_tax_total}")
# print(f"Total: ${total}")
#
# time_1 = 6
# time_2 = 10
# time_3 = 15
# speed=70
# distance_1 = speed * time_1
# distance_2 = speed * time_2
# distance_3 = speed * time_3
# print(f"The distance the car will travel in {time_1} hours: {distance_1} miles")
# print(f"The distance the car will travel in {time_2} hours: {distance_2} miles")
# print(f"The distance the car will travel in {time_3} hours: {distance_3} miles")
#
# state_sales_tax = 0.05
# county_sales_tax = 0.025
# total_sales_tax = state_sales_tax + county_sales_tax
# amount_of_purchase = float(input("Enter the amount of purchase: $ "))
# state_sales_tax_total = total_sales_tax * state_sales_tax
# county_sales_tax_total = total_sales_tax * county_sales_tax
# total_sale = amount_of_purchase + total_sales_tax
# print(f"Amount of Purchase: ${amount_of_purchase}")
# print(f"State Sales Tax: ${state_sales_tax_total}")
# print(f"County Sales Tax: ${county_sales_tax_total}")
# print(f"Total Sales Tax: ${total_sales_tax }")
# print(f"Total Sale: ${total_sale}")
#
# number_of_miles_driven = float(input("Enter the number of miles driven : "))
# gallons_of_gas_used = float(input("Enter the gallons of gas used: "))
# MPG = number_of_miles_driven / gallons_of_gas_used
# print(f"The car’s MPG is: {MPG}")

# celsius_temp = float(input("Enter the temperature in Celsius : "))
# fahrenheit_temp = float((9/5*celsius_temp)+32)
# print("The temperature in Fahrenheit : ",fahrenheit_temp)

# meal_charge = float(input("Enter the charge of the meal : "))
# tip = 0.18
# tax = 0.07
# tip_amount = tip*meal_charge
# sales_tax = tax * meal_charge
# print("Tip : ",tip_amount)
# print("Sales Tax : ",sales_tax)
# print("Total amount of meal : ", meal_charge+tip_amount+sales_tax)



car = ["A", "B", "C"]
for i in range(len(car)):
    print(f"{i + 1}. ", car[i])