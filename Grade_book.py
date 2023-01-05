last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [
  ["subjects"],
  ["grades"]
]

grades.append(100)
subjects.append("computer science")
gradebook.append(["visual arts", 93])

gradebook[-1][1]

gradebook.remove(["grades"])


gradebook.append(["Pass"])

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)