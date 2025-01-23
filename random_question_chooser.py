import codecs
import random

while True:
    start = input("Do you want to continue studying or start over? c or s\n")
    if start == "c":
        with codecs.open("save.txt", "r", "utf-8") as file:
            temp = file.read().splitlines()
        break
    elif start == "s":
        with codecs.open("questions.txt", "r", "utf-8") as file:
            temp = file.read().splitlines()
        break
    else:
        continue

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
    else:
        break

with codecs.open("save.txt", "w", "utf-8") as file:
    for question in temp:
        file.write(question + "\n")
