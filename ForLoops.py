"""
for number in range(1, 11):
    print(number)

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
for color in colors:
    print(color)
"""
"""
def powerFct(base, pow):
    result = 1
    for index in range(pow):
        result *= base
    return result

userBase = int(input("Enter your basis: "))
userPower = int(input("Enter to which power your basis should be taken: "))
your_Result = powerFct(userBase, userPower)
print(userBase, "^" , userPower, " = ", your_Result)
"""

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    for column in row:
        print(column)