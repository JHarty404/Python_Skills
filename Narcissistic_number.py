# Pythonj program for checking of
# Narcissistic number

def getResult(st):
    sum =0
    length = len(st)

    # Traversing through the string
    for i in st:

        # Coverting character to int
        sum = sum + int(i) ** length
    # Coverting string to integer
    number = int(st)
    # Comparing number and sum 
    if (number == sum):
        return "true"
    else:
        return "false"

# Driver Code
# taking input as string

st = "107"

print(getResult(st))