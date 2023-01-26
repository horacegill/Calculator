# imports the math library
import math
# gets the units entered and converts them to a float
a = float(input("First unit: "))
b = float(input("Second unit: "))
# asks for the sum type
sum = input("type of calculation (+, *, /, -, sqrt): ")
# makes the 2 numbers do the sum
if sum == "+":
    print(a + b)
elif sum == "-":
    print(a - b)
elif sum == "*":
    print(a * b)
elif sum == "/":
    print(a / b)
elif sum == "sqrt":
    print(math.sqrt(a))
    print(math.sqrt(b))
# prints the answer to the sum