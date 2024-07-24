# # create the dictionaries
# room_dictionary = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
# instructor_dictionary = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
# time_dictionary = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.',
#                    'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}
#
# # get user input for course number
# course_number = input("Enter a course number: ")
#
# # display the information for the entered course number
# print(f"Room number: {room_dictionary.get(course_number)}")
# print(f"Instructor: {instructor_dictionary.get(course_number)}")
# print(f"Meeting time: {time_dictionary.get(course_number)}")

# import random
#
# # create a dictionary of states and their capitals
# state_capitals = {
#     "Alabama": "Montgomery",
#     "Alaska": "Juneau",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
#     "California": "Sacramento",
#     "Colorado": "Denver",
#     "Connecticut": "Hartnford",
#     "Delaware": "Dover",
#     "Florida": "Tallahassee",
#     "Georgia": "Atlanta",
#     "Hawaii": "Honolulu",
#     "Idaho": "Boise",
#     "Illinois": "Springfield",
#     "Indiana": "Indianapolis",
#     "Iowa": "Des Moines",
#     "Kansas": "Topeka",
#     "Kentucky": "Frankfort",
#     "Louisiana": "Baton Rouge",
#     "Maine": "Augusta",
#     "Maryland": "Annapolis",
#     "Massachusetts": "Boston",
#     "Michigan": "Lansing",
#     "Minnesota": "St. Paul",
#     "Mississippi": "Jackson",
#     "Missouri": "Jefferson City",
#     "Montana": "Helena",
#     "Nebraska": "Lincoln",
#     "Nevada": "Carson City",
#     "New Hampshire": "Concord",
#     "New Jersey": "Trenton",
#     "New Mexico": "Santa Fe",
#     "New York": "Albany",
#     "North Carolina": "Raleigh",
#     "North Dakota": "Bismarck",
#     "Ohio": "Columbus",
#     "Oklahoma": "Oklahoma City",
#     "Oregon": "Salem",
#     "Pennsylvania": "Harrisburg",
#     "Rhode Island": "Providence",
#     "South Carolina": "Columbia",
#     "South Dakota": "Pierre",
#     "Tennessee": "Nashville",
#     "Texas": "Austin",
#     "Utah": "Salt Lake City",
#     "Vermont": "Montpelier",
#     "Virginia": "Richmond",
#     "Washington": "Olympia",
#     "West Virginia": "Charleston",
#     "Wisconsin": "Madison",
#     "Wyoming": "Cheyenne"
# }
#
# # quiz the user
# correct = 0
# incorrect = 0
#
# while True:
#     # select a random state
#     state = random.choice(list(state_capitals.keys()))
#     # user to enter the capital
#     capital = input(f"What is the capital of {state}? ")
#     # check if the answer is correct
#     if capital.lower() == state_capitals[state].lower():
#         print("Correct!")
#         correct += 1
#     else:
#         print(f"Incorrect. The capital of {state} is {state_capitals[state]}.")
#         incorrect += 1
#     again = input("Do you want to continue? (y/n) ")
#     if again.lower() != "y":
#         break
#
# # print the results
# print(f"You got {correct} out of {correct+incorrect} correct.")

# # specify the filename
# filename = "example.txt"
#
# # create an empty set to store the unique words
# unique_words = set()
#
# # read the file line by line
# with open(filename, "r") as file:
#     for line in file:
#         # split each line into a list of words
#         words = line.strip().split()
#         # add each word to the set of unique words
#         for word in words:
#             unique_words.add(word)
#
# # print the unique words
# print("Unique words found in the file:")
# for word in unique_words:
#     print(word)

# specify the filenames
input_filename = "example.txt"
output_filename = "word_frequencies.txt"

# create an empty dictionary to store the word frequencies
word_freqs = {}

# read the input file line by line
with open(input_filename, "r") as input_file:
    for line in input_file:
        # split each line into a list of words
        words = line.strip().split()
        # update the word frequencies
        for word in words:
            if word in word_freqs:
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1

# write the word frequencies to the output file
with open(output_filename, "w") as output_file:
    for word, freq in word_freqs.items():
        output_file.write(f"{word}: {freq}\n")

print("Word frequencies saved to:", output_filename)
print("Word frequencies:")

for word, freq in word_freqs.items():
    print(f"{word}: {freq}")

# import pickle
#
# # define the filename
# filename = "contacts.pickle"
#
# # try to open the pickle file
# try:
#     with open(filename, "rb") as file:
#         contacts = pickle.load(file)
# except FileNotFoundError:
#     # create an empty dictionary
#     contacts = {}
#
# # displaying the menu of options to the user
# while True:
#     print("1. Look up email address")
#     print("2. Add new contact")
#     print("3. Change email address")
#     print("4. Delete contact")
#     print("5. Quit")
#     choice = input("Enter your choice (1-5): ")
#
#     if choice == "1":
#         # looking up for email address
#         name = input("Enter name: ")
#         if name in contacts:
#             print(f"Email address: {contacts[name]}")
#         else:
#             print(f"{name} not found in contacts")
#     elif choice == "2":
#         # add a new contact
#         name = input("Enter name: ")
#         email = input("Enter email address: ")
#         contacts[name] = email
#         print(f"{name} added to contacts")
#     elif choice == "3":
#         # changing email address
#         name = input("Enter name: ")
#         if name in contacts:
#             email = input("Enter new email address: ")
#             contacts[name] = email
#             print(f"Email address for {name} updated")
#         else:
#             print(f"{name} not found in contacts")
#     elif choice == "4":
#         # delete a contact
#         name = input("Enter name: ")
#         if name in contacts:
#             del contacts[name]
#             print(f"{name} deleted from contacts")
#         else:
#             print(f"{name} not found in contacts")
#     elif choice == "5":
#         # quit the program and save the contacts to the pickle file
#         with open(filename, "wb") as file:
#             pickle.dump(contacts, file)
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice, try again")

