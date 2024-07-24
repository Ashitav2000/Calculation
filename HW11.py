# # 1
# class Employee:
#     # Initialize Employee object with name and number
#     def __init__(self, employee_name, employee_number):
#         self.__employee_name = employee_name
#         self.__employee_number = employee_number
#
#     # methods to set the employee's name, number
#     def set_employee_name(self, employee_name):
#         self.__employee_name = employee_name
#
#     def set_employee_number(self, employee_number):
#         self.__employee_number = employee_number
#
#     # Accessor methods to get the employee's name and number
#     def get_employee_name(self):
#         return self.__employee_name
#
#     def get_employee_number(self):
#         return self.__employee_number
#
#
# class ProductionWorker(Employee):
#     # Initialize ProductionWorker object using Employee's __init__ method
#     def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
#         Employee.__init__(self, employee_name, employee_number)
#         # Initialize shift number and hourly pay rate
#         self.__shift_number = shift_number
#         self.__hourly_pay_rate = hourly_pay_rate
#
#     def set_shift_number(self, shift_number):
#         self.__shift_number = shift_number
#
#     def set_hourly_pay_rate(self, hourly_pay_rate):
#         self.__hourly_pay_rate = hourly_pay_rate
#
#     def get_shift_number(self):
#         return self.__shift_number
#
#     def get_hourly_pay_rate(self):
#         return self.__hourly_pay_rate
#
#
# def main():
#     # Prompt the user for employee name, ensuring only alphabetic characters
#     employee_name = input("Enter employee name (only alphabets): ")
#     while not employee_name.isalpha():
#         employee_name = input("Invalid input. Enter employee name (only alphabets): ")
#
#     # Prompt the user for employee number, ensuring only numeric characters
#     employee_number = input("Enter employee number (only integers): ")
#     while not employee_number.isdigit():
#         employee_number = input("Invalid input. Enter employee number (only integers): ")
#     employee_number = int(employee_number)
#
#     # Prompt the user for shift number, ensuring only 1 or 2
#     shift_number = input("Enter shift number (1 for day, 2 for night): ")
#     while not shift_number.isdigit() or int(shift_number) not in [1, 2]:
#         shift_number = input("Invalid input. Enter shift number (1 for day, 2 for night): ")
#     shift_number = int(shift_number)
#
#     # Prompt the user for hourly pay rate, ensuring only numeric characters
#     hourly_pay_rate = input("Enter hourly pay rate (only integers): ")
#     while not hourly_pay_rate.isdigit():
#         hourly_pay_rate = input("Invalid input. Enter hourly pay rate (only integers): ")
#     hourly_pay_rate = int(hourly_pay_rate)
#
#     worker = ProductionWorker(employee_name, employee_number, shift_number, hourly_pay_rate)
#
#     # Display the employee information
#     print("\nEmployee Information:")
#     print("Name:", worker.get_employee_name())
#     print("Number:", worker.get_employee_number())
#     print("Shift:", "Day" if worker.get_shift_number() == 1 else "Night")
#     print("Hourly Pay Rate:", worker.get_hourly_pay_rate())
#
#
# if __name__ == "__main__":
#     main()


# 2
# class Employee:
#     # Initialize the Employee class with name and number
#     def __init__(self, employee_name, employee_number):
#         self.__employee_name = employee_name
#         self.__employee_number = employee_number
#
#     # methods to set the employee's name and number
#     def set_employee_name(self, employee_name):
#         self.__employee_name = employee_name
#
#     def set_employee_number(self, employee_number):
#         self.__employee_number = employee_number
#
#     # methods to get the employee's name and number
#     def get_employee_name(self):
#         return self.__employee_name
#
#     def get_employee_number(self):
#         return self.__employee_number
#
#
# class ShiftSupervisor(Employee):
#     # Initialize the ShiftSupervisor class with name, number, annual salary, and bonus
#     def __init__(self, employee_name, employee_number, annual_salary, annual_production_bonus):
#         # Call the Employee class's initializer to set the name and number
#         Employee.__init__(self, employee_name, employee_number)
#         self.__annual_salary = annual_salary
#         self.__annual_production_bonus = annual_production_bonus
#
#     def set_annual_salary(self, annual_salary):
#         self.__annual_salary = annual_salary
#
#     def set_annual_production_bonus(self, annual_production_bonus):
#         self.__annual_production_bonus = annual_production_bonus
#
#     def get_annual_salary(self):
#         return self.__annual_salary
#
#     def get_annual_production_bonus(self):
#         return self.__annual_production_bonus
#
#
# def main():
#     # Prompt the user for supervisor's name, ensuring only alphabetic characters
#     employee_name = input("Enter supervisor name (only alphabets): ")
#     while not employee_name.isalpha():
#         employee_name = input("Invalid input. Enter supervisor name (only alphabets): ")
#
#     # Prompt the user for supervisor's number, ensuring only numeric characters
#     employee_number = input("Enter supervisor number (only integers): ")
#     while not employee_number.isdigit():
#         employee_number = input("Invalid input. Enter supervisor number (only integers): ")
#     employee_number = int(employee_number)
#
#     # Prompt the user for supervisor's annual salary, ensuring only numeric characters
#     annual_salary = input("Enter annual salary (only integers): ")
#     while not annual_salary.isdigit():
#         annual_salary = input("Invalid input. Enter annual salary (only integers): ")
#     annual_salary = int(annual_salary)
#
#     # Prompt the user for supervisor's annual production bonus, ensuring only numeric characters
#     annual_production_bonus = input("Enter annual production bonus (only integers): ")
#     while not annual_production_bonus.isdigit():
#         annual_production_bonus = input("Invalid input. Enter annual production bonus (only integers): ")
#     annual_production_bonus = int(annual_production_bonus)
#
#     supervisor = ShiftSupervisor(employee_name, employee_number, annual_salary, annual_production_bonus)
#
#     # Display the shift supervisor's information
#     print("\nShift Supervisor Information:")
#     print("Name:", supervisor.get_employee_name())
#     print("Number:", supervisor.get_employee_number())
#     print("Annual Salary:", supervisor.get_annual_salary())
#     print("Annual Production Bonus:", supervisor.get_annual_production_bonus())
#
#
# if __name__ == "__main__":
#     main()


# 3
class Person:
    def __init__(self, name, address, phone_number):
        # Initialize a Person object with name, address, and phone number
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    # methods to set the person's name, address and phone number
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # methods to get the person's name, address and phone number
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number


class Customer(Person):
    # Initialize a Customer object using the Person class's initializer
    def __init__(self, name, address, phone_number, customer_number, mailing_list):
        Person.__init__(self, name, address, phone_number)
        # Also set the customer number and mailing list flag
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def is_on_mailing_list(self):
        return self.__mailing_list


def main():
    # Prompt the user for the customer's name, ensuring only alphabetic characters
    name = input("Enter customer name (only alphabets): ")
    while not name.isalpha():
        name = input("Invalid input. Enter customer name (only alphabets): ")

    # Prompt the user for the customer's address
    address = input("Enter customer address: ")

    # Prompt the user for the customer's phone number, ensuring only numeric characters
    phone_number = input("Enter customer phone number (only digits): ")
    while not phone_number.isdigit():
        phone_number = input("Invalid input. Enter customer phone number (only digits): ")

    # Prompt the user for the customer's number, ensuring only numeric characters
    customer_number = input("Enter customer number (only digits): ")
    while not customer_number.isdigit():
        customer_number = input("Invalid input. Enter customer number (only digits): ")
    customer_number = int(customer_number)

    # Prompt the user if the customer should be on the mailing list, ensuring a yes or no response
    mailing_list_input = input("Should the customer be on the mailing list? (yes/no): ").lower()
    while mailing_list_input not in ['yes', 'no']:
        mailing_list_input = input("Invalid input. Should the customer be on the mailing list? (yes/no): ").lower()
    mailing_list = mailing_list_input == 'yes'

    customer = Customer(name, address, phone_number, customer_number, mailing_list)

    # Display the customer information
    print("\nCustomer Information:")
    print("Name:", customer.get_name())
    print("Address:", customer.get_address())
    print("Phone Number:", customer.get_phone_number())
    print("Customer Number:", customer.get_customer_number())
    print("On Mailing List:", "Yes" if customer.is_on_mailing_list() else "No")


if __name__ == "__main__":
    main()
