import tkinter as tk
import os
import random
from tkinter import filedialog
from cryptography.fernet import Fernet


def fileto_processing():
    # Take the file name
    nameof_file = file_entry.get()

    # Add .txt extension to the file
    nameof_file = nameof_file + ".txt"

    # Check file exist or not
    if os.path.isfile(nameof_file):
        print("File processing:", nameof_file)
        return nameof_file
    else:
        print("File not available. Create an empty file:", file_name)
        with open(nameof_file, 'w') as f:
            pass

        # Append numbers into the file
    with open(nameof_file, 'a') as f:
        for i in range(10):
            random_num = random.randint(1, 100)
            f.write(str(random_num) + '\n')

    # Return file name for use by display_file_data function
    return nameof_file


def filter_datain_file():
    nameof_file = file_entry.get()
    nameof_file = nameof_file + ".txt"
    # Check if a file has been specified
    # if not file_name:
    #     print("No file specified. Please enter a file name and click Process File.")
    #     return
    try:
        with open(nameof_file, 'r') as f:
            numbers = f.readlines()
            numbers = [int(x.strip()) for x in numbers]
            numbers.sort()

            # Display sorted numbers to user
            result_text = "Filtered Numbers: {}".format(numbers)
            result_label.config(text=result_text)
    except FileNotFoundError:
        result_text = "Error file not found"
        result_label.config(text=result_text)


def show_datain_file():
    nameof_file = file_entry.get()
    nameof_file = nameof_file + ".txt"

    # Check if a file has been specified
    # if not file_name:
    #     print("No file specified. Please enter a file name and click Process File.")
    #     return
    try:
        with open(nameof_file, 'r') as f:
            # numbers = f.read().splitlines()
            numbers = f.readlines()
            numbers = [int(x.strip()) for x in numbers]
            total = sum(int(num) for num in numbers)
            if total == 0:
                average = 0
            else:
                average = total / len(numbers)

            # Display results to user
            result_text = "Number: {}\nTotal: {}\nAverage: {:.2f}".format(numbers, total, average)
            result_label.config(text=result_text)
    except FileNotFoundError:
        result_text = "Not Found"
        result_label.config(text=result_text)


def find_number():
    nameof_file = file_entry.get()
    nameof_file = nameof_file + ".txt"
    search_num = num_entry.get()

    try:
        with open(nameof_file, "r") as file:
            count = 0
            for line in file:
                numbers = line.strip().split()
                for num in numbers:
                    print(num)
                    if int(num) == int(search_num):
                        print("Data Found")
                        count += 1
            result_text = f"The {search_num} occured {count} times"
            result_label.config(text=result_text)

    except FileNotFoundError:
        result_text = "Not Found"
        result_label.config(text=result_text)


def highest_number():
    filename = file_entry.get()
    filename = filename + ".txt"
    try:
        with open(filename, "r") as file:
            largest_num = -float('inf')
            for line in file:
                numbers = line.strip().split()
                for num in numbers:
                    if int(num) > largest_num:
                        largest_num = int(num)
            result_text = f"The highest number in the data file is {largest_num}."
            result_label.config(text=result_text)
    except FileNotFoundError:
        result_text = "Error occured."
        result_label.config(text=result_text)


def numberto_append():
    nameof_file = file_entry.get()
    nameof_file = nameof_file + ".txt"
    try:
        with open(nameof_file, "a") as file:
            num_to_append = random.randint(1, 10)
            for i in range(num_to_append):
                random_num = random.randint(1, 100)
                file.write(f"{random_num}\n")

        result_text = f"{num_to_append} random numbers have been appended to the data file."
        result_label.config(text=result_text)
    except FileNotFoundError:
        result_text = "Error occured."
        result_label.config(text=result_text)


# create a function to encrypt a file
def file_encryption():
    # ask the user to select a file
    file_path = file_entry.get()
    file_path = file_path + ".txt"

    # read the contents of the file
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        result_text = f"File not found."
        result_label.config(text=result_text)

        # generate a Fernet key or load the existing key from a file
    try:
        key = load_key()
    except FileNotFoundError:
        generate_key()
        key = load_key()


    cipher_suite = Fernet(key)

    # encrypt the data and write it to a new file
    encrypted_data = cipher_suite.encrypt(data)
    with open(file_path + ".encrypted", 'wb') as f:
        f.write(encrypted_data)

    # display a message
    result_text = f"Encryption completed. {key} is the key"
    result_label.config(text=result_text)

def key_generation():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# fuAction to load the key from a file
def key_loading():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def file_decryption():
    # ask the user to select a file
    file_path = file_entry.get()
    file_path = file_path + ".txt"
    # read the contents of the file
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        result_text = f"File not found."
        result_label.config(text=result_text)
        # load the key from a file
    try:
        key = load_key()
    except FileNotFoundError:
        tk.messagebox.showerror("Error in the Key", "The key is not found.")
        return

    cipher_suite = Fernet(key.decode())

    # decrypt the data and write it to a new file
    decrypted_data = cipher_suite.decrypt(data)
    with open(file_path + ".decrypted", 'wb') as f:
        f.write(decrypted_data)

    # display a message
    result_text = f"Decryption is done."
    result_label.config(text=result_text)


def end_gui():
    root.destroy()


# Creating main
root = tk.Tk()
root.title("Final Project")
root.geometry("800x800")

main_label = tk.Label(root, text="UNH Scripting w/Python", font=("Arial", 14))
main_label.pack(pady=15)

# File for entry field and label creation
file_label = tk.Label(root, text="File Name (without any extension):",fg = 'Yellow', bg = 'Black')
file_label.pack(pady=8)
file_entry = tk.Entry(root)
file_entry.pack(pady=8)

# Creating the  process button
process_button = tk.Button(root, text="File Processing",fg = 'Green', bg = 'Black', command=fileto_processing)
process_button.pack(pady=12)

# display button Creation
display_button = tk.Button(root, text="Show the Data", command=show_datain_file)
display_button.pack(pady=12)

# Sort button creation
sort_button = tk.Button(root, text="Sort the file", command=filter_datain_file)
sort_button.pack(pady=12)
# Creating a number label
num_label = tk.Label(root, text="Give the number to find:")
num_label.pack(pady=7)
num_entry = tk.Entry(root)
num_entry.pack(pady=7)
# Searching the number
search_button = tk.Button(root, text="Find the number",fg = 'White', bg = 'Purple', command=find_number)
search_button.pack(pady=12)
# Finding the highest number available
large_button = tk.Button(root, text="Highest Number in the file ",fg = 'Yellow', bg = 'Blue', command=highest_number)
large_button.pack(pady=12)

append_button = tk.Button(root, text="Append the Number", command=numberto_append)
append_button.pack(pady=12)
# Creating File encryption button
encrypt_button = tk.Button(root, text='File Encryption',fg = 'Yellow', bg = 'Black', command=file_encryption)
encrypt_button.pack(pady=12)
# Creating File Decryption button
decrypt_button = tk.Button(root, text='Decrypt the File',fg = 'Yellow', bg = 'Black',command=file_decryption)
decrypt_button.pack(pady=12)
# Exit button
exit_button = tk.Button(root, text="Stop",fg = 'Black', bg = 'Red', command=end_gui)
exit_button.pack(pady=18)

# Displaying the results
result_label = tk.Label(root, text="")
result_label.pack(pady=12)

# Initiate the GUI loop
root.mainloop()