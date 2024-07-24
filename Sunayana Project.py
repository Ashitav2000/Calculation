# Python Project
# Sunayana Katha(00768885)
# 05/03/2023

import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import random
import base64


class PythonScriptingProject:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='white')
        self.master.title("UNH Scripting w/Python")
        self.file_path = None

        # Create widgets
        self.label_title = tk.Label(self.master, text="UNH Scripting w/Python")
        self.label_file = tk.Label(self.master, text="Current data file being processed:")

        self.select_file_button = tk.Button(self.master, text="Select File", command=self.select_file)
        self.display_all_button = tk.Button(self.master, text="Display all", command=self.display_all)
        self.sort_button = tk.Button(self.master, text="Sort", command=self.sort_numbers)
        self.search_occurs_button = tk.Button(self.master, text="Search/Occurs", command=self.search_occurs)
        self.largest_button = tk.Button(self.master, text="Largest", command=self.largest)
        self.append_number_button = tk.Button(self.master, text="Append Number", command=self.append_number)
        self.encrypt_button = tk.Button(self.master, text="Encrypt", command=self.encrypt)
        self.decrypt_button = tk.Button(self.master, text="DeCrypt", command=self.decrypt)
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)

        # Place widgets
        self.label_title.grid(row=0, column=0, columnspan=2)
        self.label_file.grid(row=1, column=0, columnspan=2)

        self.select_file_button.grid(row=2, column=0)
        self.display_all_button.grid(row=3, column=0)
        self.sort_button.grid(row=4, column=0)
        self.search_occurs_button.grid(row=5, column=0)
        self.largest_button.grid(row=6, column=0)
        self.append_number_button.grid(row=7, column=0)
        self.encrypt_button.grid(row=8, column=0)
        self.decrypt_button.grid(row=9, column=0)
        self.exit_button.grid(row=10, column=0)

    def select_file(self):
        file_name = simpledialog.askstring("Enter File Name",
                                           "Enter the part of the filename preceding the .txt extension:")
        if file_name:
            file_name = file_name.strip() + '.txt'
            if not os.path.exists(file_name):
                open(file_name, 'w').close()
            self.file_path = file_name
            print(file_name)
            self.label_file.config(text=f"Current data file being processed: {os.path.basename(self.file_path)}")

    def display_all(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            numbers = [int(line.strip()) for line in lines if line.strip().isdigit()]

        total = sum(numbers)
        average = total / len(numbers)

        tk.messagebox.showinfo("Display All", f"Numbers: {numbers}\nTotal: {total}\nAverage: {average:.2f}")

    def sort_numbers(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            numbers = sorted([int(line.strip()) for line in lines if line.strip().isdigit()])

        tk.messagebox.showinfo("Sorted Numbers", f"Sorted numbers: {numbers}")

    def search_occurs(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        search_number = simpledialog.askinteger("Search", "Enter the number you want to search for:")
        if search_number is None:
            return

        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            numbers = [int(line.strip()) for line in lines if line.strip().isdigit()]

        count = numbers.count(search_number)
        tk.messagebox.showinfo("Search/Occurs", f"Number {search_number} occurs {count} time(s).")

    def largest(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            numbers = [int(line.strip()) for line in lines if line.strip().isdigit()]

        largest_number = max(numbers)
        tk.messagebox.showinfo("Largest", f"Largest number: {largest_number}")

    def append_number(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        n = simpledialog.askinteger("Append", "How many random numbers do you want to append?")
        if n is None:
            return

        random_numbers = [random.randint(1, 100) for _ in range(n)]

        with open(self.file_path, 'a') as file:
            for number in random_numbers:
                file.write(str(number) + '\n')

        tk.messagebox.showinfo("Append Number", f"Appended {n} random number(s).")

    def encrypt(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        with open(self.file_path, 'r') as file:
            content = file.read()

        encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

        with open(self.file_path, 'w') as file:
            file.write(encoded_content)

        tk.messagebox.showinfo("Encrypt", "File encrypted successfully.")

    def decrypt(self):
        if not self.file_path:
            tk.messagebox.showerror("Error", "No file selected.")
            return

        with open(self.file_path, 'r') as file:
            content = file.read()

        try:
            decoded_content = base64.b64decode(content.encode('utf-8')).decode('utf-8')
        except Exception:
            tk.messagebox.showerror("Error", "Decryption failed. The file might not be encrypted or is corrupted.")
            return

        with open(self.file_path, 'w') as file:
            file.write(decoded_content)

        tk.messagebox.showinfo("Decrypt", "File decrypted successfully.")


def main():
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 1.0)  # Set scaling to 100% to improve widget appearance
    root.tk.call('option', 'add', '*font', 'Helvetica')  # Set default font to Helvetica
    app = PythonScriptingProject(root)
    root.mainloop()


if __name__ == '__main__':
    main()