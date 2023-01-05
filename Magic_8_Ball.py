import random

name = "Josh"
question = "Will i get a Tesla"
answer = ""

random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes !"

elif random_number == 2:
    answer = " No dopubt."

elif random_number == 3:
    answer = " it is unclear."

elif random_number == 4:
    answer = "My feeling is no "

elif random_number == 5:
    answer = "This is possable."

elif random_number == 6:
    answer = "You don't want the answer"

elif random_number == 7:
    answer = "No Chance"

elif random_number == 8:
    answer = "Chances are slim"

elif random_number == 9:
    answer = "tHIS IS DECIDED !"

else:
    answer =- "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)


