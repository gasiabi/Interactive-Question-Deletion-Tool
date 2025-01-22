import codecs
import random

with codecs.open("questions.txt", "r", "utf-8") as file:
    temp = file.read().splitlines()

while len(temp) != 0:
    print("The number of questions:", len(temp))
    selected = random.choice(temp)
    print(selected)
    answer = input("Delete the question? y or n\n")
    if answer == "y":
        temp.remove(selected)
        print("Good job! The question got deleted.\n")
    elif answer == "n":
        print("Good luck next time! The question is still in the system.\n")
        continue

