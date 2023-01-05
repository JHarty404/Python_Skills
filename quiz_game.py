print("Welcome to my computor quiz")

playing = input("Do you want to play ?: ")

if playing.upper()  != "yes":
    quit()
    
    print("Okay! Lets play!")
    score = 0

answer = input("what does CPU stand for ?: ")
if answer.upper() == "centrol processing unit ":
    print('Correct')
    score += 1
else:
    print("wrong!!!!!!")

    answer = input("What does GPU stand for ?: ")
if answer.upper() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect")



    answer = input("what does RAM stand for ?: ")
if answer.upper()== "random access memory":
    print('Correct')
    score += 1

else:
    print("Incorrect")

answer = input("what does  PSU stand for ?: ")
if answer.upper() == "power supply":
    print('Correct')
    score += 1
else:
    print("Incorrect")
    
print("You got" + str(score) + " queston correct !")







