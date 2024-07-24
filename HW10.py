# # 1
# class Pet:
#     def __init__(self):
#         self.__name = "name"
#         self.__animal_type = "animal_type"
#         self.__age = 0
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_animal_type(self, animal_type):
#         self.__animal_type = animal_type
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_animal_type(self):
#         return self.__animal_type
#
#     def get_age(self):
#         return self.__age
#
#
# # Sample program to create a Pet object and prompt user for details
# def main():
#     # create a pet object
#     my_pet = Pet()
#
#     # Prompt user for pet details
#     name = input("Enter the name of your pet: ")
#     animal_type = input("Enter the type of animal your pet is: ")
#     age = int(input("Enter the age of your pet: "))
#
#     # Set the pet's attributes
#     my_pet.set_name(name)
#     my_pet.set_animal_type(animal_type)
#     my_pet.set_age(age)
#
#     # Display the pet's details
#     print("\nPet's Details:")
#     print("Name:", my_pet.get_name())
#     print("Animal Type:", my_pet.get_animal_type())
#     print("Age:", my_pet.get_age())
#
#
# if __name__ == "__main__":
#     main()


# 2
# class Car:
#     def __init__(self, year_model, make):
#         self.__year_model = year_model
#         self.__make = make
#         self.__speed = 0
#
#     def accelerate(self):
#         self.__speed += 5
#
#     def brake(self):
#         self.__speed -= 5
#         if self.__speed < 0:
#             self.__speed = 0
#
#     def get_speed(self):
#         return self.__speed
#
#
# def main():
#     # create a car object
#     my_car = Car(2022, "Toyota")
#
#     # accelerate the car five times and display the speed after each acceleration
#     print("Accelerating...")
#     for _ in range(5):
#         my_car.accelerate()
#         print("Current Speed:", my_car.get_speed())
#
#     # brake the car five times and display the speed after each braking
#     print("\nBraking...")
#     for _ in range(5):
#         my_car.brake()
#         print("Current Speed:", my_car.get_speed())
#
#
# if __name__ == "__main__":
#     main()


# 3
class Question:
    # Initialize attributes for the question and its possible answers
    def __init__(self, question, ans1, ans2, ans3, ans4, correct_answer):
        self.question = question
        self.answer1 = ans1
        self.answer2 = ans2
        self.answer3 = ans3
        self.answer4 = ans4
        self.correct_answer = correct_answer

    def __str__(self):
        return f"Question: {self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}"


class TrivialGame:
    def __init__(self):
        # List of 10 trivia questions
        self.questions = [
            Question("What is the capital of Italy?", "A. London", "B. Kyiv", "C. Rome", "D. Berlin", 3),
            Question("What is the capital of England?", "A. London", "B. Paris", "C. Belgium", "D. Berlin", 1),
            Question("What is the capital of India?", "A. Kyiv", "B. New Delhi", "C. Rome", "D. Berlin", 1),
            Question("What is the capital of Germany?", "A. London", "B. Paris", "C. Sanaa", "D. Berlin", 4),
            Question("What is the capital of USA?", "A. Washinton D.C", "B. Dhaka", "C. Rome", "D. Sanaa", 1),
            Question("What is the capital of Bangladesh?", "A. London", "B. Paris", "C. Rome", "D. Dhaka", 4),
            Question("What is the capital of Russia?", "A. London", "B. Moscow", "C. Sanaa", "D. New Delhi", 2),
            Question("What is the capital of Ukraine?", "A. Kyiv", "B. Paris", "C. Warsaw", "D. Dhaka", 1),
            Question("What is the capital of Pakistan?", "A. London", "B. Kyiv", "C. Islamabad", "D. Berlin", 3),
            Question("What is the capital of UAE?", "A. Dubai", "B. Paris", "C. Rome", "D. New Delhi", 1),
        ]

    def game_play(self):
        score_points = [0, 0]
        # Player 1's turn
        for i in range(5):
            print(f"\nQuestion {i+1}:")
            print(self.questions[i])
            player_1_answer = int(input("Player 1, enter your answer (1-4): "))
            if player_1_answer == self.questions[i].correct_answer:
                score_points[0] += 1

            # Player 2's turn
            print(f"\nQuestion {i+6}:")
            print(self.questions[i+5])
            player_2_answer = int(input("Player 2, enter your answer (1-4): "))
            if player_2_answer == self.questions[i+5].correct_answer:
                score_points[1] += 1

        # # Display final scores and determine the winner
        print("\nGame over!")
        print(f"Player 1 score: {score_points[0]}")
        print(f"Player 2 score: {score_points[1]}")
        if score_points[0] > score_points[1]:
            print("Player 1 wins!")
        elif score_points[0] < score_points[1]:
            print("Player 2 wins!")
        else:
            print("It's a tie!")


# Main program
my_game = TrivialGame()
my_game.game_play()
