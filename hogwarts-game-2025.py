import random
import time

print("Welcome to The School of Hogwarts game!")
time.sleep(2)

user_name = input("What's your name? ")

# List of houses to be sorted
houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

print(f"Be prepared {user_name}, you will be from house: ")
time.sleep(2.5)

# Randomly choosing a house for the user
chosen_house = random.choice(houses)
print(f"Your house is: {chosen_house} ")
time.sleep(2)

# Counting house scores
gryffindor_count = 0
ravenclaw_count = 0
hufflepuff_count = 0
slytherin_count = 0

print("\nThis is a lucky game, if you pick the wrong number, your house doesn't get points.")

# Question 1
while True:
    try:
        question_1 = int(input("Question 1) Do you like Dawn or Dusk?\nPress 1 for Dawn\nPress 2 for Dusk: "))

        if question_1 == 1:
            gryffindor_count += 1
            ravenclaw_count += 1
        elif question_1 == 2:
            hufflepuff_count += 1
            slytherin_count += 1
        else:
            print("You must pick a number between 1 and 2.")
            continue  # Repeat the loop if input is invalid

        break  # Exit the loop when input is valid

    except ValueError:
        print("Please enter a valid number (1 or 2).")

# Question 2
while True:
    try:
        question_2 = int(input("\nQ2) When I’m dead, I want people to remember me as:\n1 - The good\n2 - The Great\n3 - The Wise\n4 - The Bold\nChoose (1-4): "))

        if question_2 == 1:
            hufflepuff_count += 2
        elif question_2 == 2:
            slytherin_count += 2
        elif question_2 == 3:
            ravenclaw_count += 2
        elif question_2 == 4:
            gryffindor_count += 2
        else:
            print("You must pick a number between 1 and 4.")
            continue  # Repeat the loop if input is invalid

        break  # Exit the loop when input is valid

    except ValueError:
        print("Pick a whole number between 1 and 4.")

# Question 3
print("\nFinal question")
time.sleep(2)

while True:
    try:
        question_3 = int(input("\nQ3) Which kind of instrument most pleases your ear?\n1 - Violin\n2 - Trumpet\n3 - Piano\n4 - Drum\nChoose (1-4): "))

        if question_3 == 1:
            slytherin_count += 4
        elif question_3 == 2:
            hufflepuff_count += 4
        elif question_3 == 3:
            ravenclaw_count += 4
        elif question_3 == 4:
            gryffindor_count += 4
        else:
            print(" You must pick a number between 1 and 4.")
            continue  # Repeat the loop if input is invalid

        break  # Exit the loop when input is valid

    except ValueError:
        print(" Please pick a whole number between 1 and 4.")

# Display final scores
print("\nFinal House Points:")
print(f"Gryffindor: {gryffindor_count}")
print(f"Ravenclaw: {ravenclaw_count}")
print(f"Hufflepuff: {hufflepuff_count}")
print(f"Slytherin: {slytherin_count}")
time.sleep(2)

# Determine the winning house
house_winner = None

if slytherin_count > hufflepuff_count and slytherin_count > ravenclaw_count and slytherin_count > gryffindor_count:
    house_winner = "Slytherin"
elif gryffindor_count > hufflepuff_count and gryffindor_count > ravenclaw_count and gryffindor_count > slytherin_count:
    house_winner = "Gryffindor"
elif ravenclaw_count > hufflepuff_count and ravenclaw_count > gryffindor_count and ravenclaw_count > slytherin_count:
    house_winner = "Ravenclaw"
elif hufflepuff_count > gryffindor_count and hufflepuff_count > ravenclaw_count and hufflepuff_count > slytherin_count:
    house_winner = "Hufflepuff"
else:
    house_winner = "tie"

# Display results
if house_winner == "tie":
    print("It's a tie. Try again.")
else:
    print(f"The winner house is {house_winner}!")

if chosen_house == house_winner:
    print(" Congratulations! Your house is the winner!")
else:
    print("Better luck next time.")