import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
import base64


class PythonScriptingProject:
    def __init__(self, root):
        self.root = root
        self.filename = ""

    def select_create_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if not os.path.exists(self.filename):
            with open(self.filename, 'w'):
                pass
        messagebox.showinfo("File Selected", f"{self.filename} selected successfully!")

    def display_all(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        with open(self.filename, 'r') as file:
            numbers = file.readlines()
            if numbers:
                numbers = [float(num.strip()) for num in numbers]
                total = sum(numbers)
                average = total / len(numbers)
                messagebox.showinfo("Display All", f"Numbers: {numbers}\nTotal: {total}\nAverage: {average}")
            else:
                messagebox.showinfo("Display All", "The file is empty.")

    def display_sorted(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        with open(self.filename, 'r') as file:
            numbers = file.readlines()
            if numbers:
                numbers = sorted([float(num.strip()) for num in numbers])
                messagebox.showinfo("Display Sorted", f"Numbers: {numbers}")
            else:
                messagebox.showinfo("Display Sorted", "The file is empty.")

    def search_occurs(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        target = simpledialog.askfloat("Search", "Enter the number to search:")
        with open(self.filename, 'r') as file:
            numbers = file.readlines()
            occurs = numbers.count(f"{target}\n")
            messagebox.showinfo("Search", f"Number {target} occurs {occurs} times.")

    def display_largest(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        with open(self.filename, 'r') as file:
            numbers = file.readlines()
            if numbers:
                largest = max([float(num.strip()) for num in numbers])
                messagebox.showinfo("Largest", f"Largest number is {largest}")
            else:
                messagebox.showinfo("Largest", "The file is empty.")

    def append_number(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        number = simpledialog.askfloat("Append", "Enter number to append:")
        with open(self.filename, 'a') as file:
            file.write(f"{number}\n")
        messagebox.showinfo("Append", "Number appended successfully.")

    def encrypt(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        with open(self.filename, 'r') as file:
            content = file.read()
        encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        with open(self.filename, 'w') as file:
            file.write(encoded_content)
        messagebox.showinfo("Encrypt", "File encrypted successfully.")

    def decrypt(self):
        if not self.filename:
            messagebox.showerror("Error", "Please select/create a data file first.")
            return
        with open(self.filename, 'r') as file:
            content = file.read()
        try:
            decoded_content = base64.b64decode(content.encode('utf-8')).decode('utf-8')
        except ValueError:
            messagebox.showerror("Error", "Decryption failed. The file might not be encrypted or is corrupted.")
            return
        with open(self.filename, 'w') as file:
            file.write(decoded_content)
        messagebox.showinfo("Decrypt", "File decrypted successfully.")


def main():
    root = tk.Tk()
    root.title("UNH Scripting w/Python")
    app = PythonScriptingProject(root)
    tk.Label(root, text="UNH Scripting w/Python").pack()
    # tk.Label(root, textvariable=app.filename).pack()
    tk.Button(root, text="Select/Create File", command=app.select_create_file).pack()
    tk.Button(root, text="Display All", command=app.display_all).pack()
    tk.Button(root, text="Display Sorted", command=app.display_sorted).pack()
    tk.Button(root, text="Search/Occurs", command=app.search_occurs).pack()
    tk.Button(root, text="Display Largest", command=app.display_largest).pack()
    tk.Button(root, text="Append Number", command=app.append_number).pack()
    tk.Button(root, text="Encrypt", command=app.encrypt).pack()
    tk.Button(root, text="Decrypt", command=app.decrypt).pack()
    tk.Button(root, text="Exit", command=root.quit).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
