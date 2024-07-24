# FinalExam-Script Programming/Python
# Name: Ashita Vemulapalli
# Email: avemu11@unh.newhaven.edu
# ID: 00876806
# 05/02/2024

# CODE

import tkinter as tk
from collections import defaultdict
from tkinter import messagebox


# Define a class for the application
class FinalExam:
    # Initialize the application
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        # Set the scaling factor for the window
        self.window.geometry("300x300")
        self.window.title("Final Exam Index")
        # Create a label for the file name entry
        self.entry_label = tk.Label(self.window, text="Enter file name:", fg='Black', bg='BurlyWood',)
        self.entry_label.pack()

        # Create an entry field for the file name
        self.file_entry = tk.Entry(self.window)
        self.file_entry.pack()

        # Create a button to analyze the file
        self.analyze_button = tk.Button(self.window, text="Analyze", fg='Black', bg='CornflowerBlue',
                                        command=self.analyze_the_file)
        self.analyze_button.pack()

        # Create a button to quit the application
        self.quit_button = tk.Button(self.window, text="Quit", fg='Black', bg='Aquamarine',
                                     command=self.quit_the_program)
        self.quit_button.pack()

        # Create a listbox to display the results
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack()

    # Define the method to analyze the file
    def analyze_the_file(self):
        # Get the file name from the entry field and add the .txt extension
        file_name = self.file_entry.get() + ".txt"
        try:
            # Open the file and read the lines
            with open(file_name, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            # Show an error message if the file is not found
            messagebox.showerror("Error", "File not found.")
            return

        # Create a dictionary to store the words and their line numbers
        word_dict = defaultdict(set)
        for i, line in enumerate(lines, start=1):
            words = line.split()
            for word in words:
                word_dict[word].add(i)

        # Write the words and their line numbers to the index file
        with open('index.txt', 'w') as index_file:
            for word in sorted(word_dict.keys()):
                index_file.write(f"{word}:\n")
                for line_number in sorted(word_dict[word]):
                    index_file.write(f"{line_number}\n")

        # Update the listbox with the words and their line numbers
        self.listbox.delete(0, tk.END)
        for word in sorted(word_dict.keys()):
            self.listbox.insert(tk.END, f"{word}: {'  '.join(map(str, sorted(word_dict[word])))}")

    # Define the method to quit the application
    def quit_the_program(self):
        self.window.destroy()

    # Define the method to run the application
    def run(self):
        self.window.mainloop()


# Run the application
if __name__ == "__main__":
    analyzer = FinalExam()
    analyzer.run()
