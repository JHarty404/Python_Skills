single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []

for item in single_digits:
    print(item)
    squares.append(item**2)
print(squares)

cubes = [items**3 for items in single_digits]
print(cubes)