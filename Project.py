# Final Project

# Name: Ashita Vemulapalli
# Email: avemu11@unh.newhaven.edu
# ID: 00876806

import tkinter as tk
from tkinter import messagebox
import os


def select_or_create_file():
    name_of_file = file_entry.get() + ".txt"
    if not os.path.exists(name_of_file):
        with open(name_of_file, 'w'):
            pass
        messagebox.showinfo("File is created", f"The file '{name_of_file}' has been created successfully.")
    else:
        messagebox.showerror("File already exists", f"The file '{name_of_file}' already exists.")


def display_all_numbers():
    name_of_file = file_entry.get() + ".txt"
    if os.path.exists(name_of_file):
        with open(name_of_file, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            total = sum(numbers)
            average = total / len(numbers) if numbers else 0
            messagebox.showinfo("File Content", f"Numbers: {numbers}\nTotal: {total}\nAverage: {average}")
    else:
        messagebox.showerror("File Not Found", "Please select/create a data file first.")


def display_sorted_numbers():
    name_of_file = file_entry.get() + ".txt"
    if os.path.exists(name_of_file):
        with open(name_of_file, 'r') as file:
            numbers = sorted([int(line.strip()) for line in file])
            messagebox.showinfo("Sorted Numbers", f"Sorted Numbers: {numbers}")
    else:
        messagebox.showerror("File Not Found", "Please select/create a data file first.")


def search_occurrences():
    name_of_file = file_entry.get() + ".txt"
    if os.path.exists(name_of_file):
        search_num = int(input("Enter number to search: "))
        with open(name_of_file, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            count = numbers.count(search_num)
            messagebox.showinfo("Search Result", f"Number of occurrences of {search_num}: {count}")
    else:
        messagebox.showerror("File Not Found", "Please select/create a data file first.")


def display_largest_number():
    file_name = file_entry.get() + ".txt"
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            largest = max(numbers) if numbers else None
            messagebox.showinfo("Largest Number", f"Largest Number: {largest}")
    else:
        messagebox.showerror("File Not Found", "Please select/create a data file first.")


def append_numbers():
    file_name = file_entry.get() + ".txt"
    if os.path.exists(file_name):
        number = int(input("Enter the number to append: "))
        with open(file_name, 'a') as file:
            file.write(str(number) + '\n')
        messagebox.showinfo("Number Appended", f"Number {number} has been appended to the file.")
    else:
        messagebox.showerror("File Not Found", "Please select/create a data file first.")


def encrypt_file():
    pass


def decrypt_file():
    pass


def exit_program():
    window.destroy()


# GUI setup
window = tk.Tk()
window.title("UNH Scripting w/Python")

label = tk.Label(window, text="UNH Scripting w/Python", fg='Yellow', bg='Blue')
label.pack()

file_label = tk.Label(window, text="Current data file being processed:")
file_label.pack()

file_entry = tk.Entry(window)
file_entry.pack()

button_create_file = tk.Button(window, text="Select/Create Data File", fg='Green',
                               bg='Yellow', command=select_or_create_file)
button_create_file.pack()

button_display_all = tk.Button(window, text="Display All", fg='White',
                               bg='Purple', command=display_all_numbers)
button_display_all.pack()

button_display_sorted = tk.Button(window, text="Display Sorted",
                                  fg='Black', bg='Yellow', command=display_sorted_numbers)
button_display_sorted.pack()

button_search_occurs = tk.Button(window, text="Search/Occurs", command=search_occurrences)
button_search_occurs.pack()

button_display_largest = tk.Button(window, text="Largest", command=display_largest_number)
button_display_largest.pack()

button_append_number = tk.Button(window, text="Append Number", command=append_numbers)
button_append_number.pack()

button_encrypt_file = tk.Button(window, text="Encrypt", command=encrypt_file)
button_encrypt_file.pack()

button_decrypt_file = tk.Button(window, text="Decrypt", command=decrypt_file)
button_decrypt_file.pack()

button_exit = tk.Button(window, text="Exit", fg='Black', bg='Red', command=exit_program)
button_exit.pack()

window.mainloop()
