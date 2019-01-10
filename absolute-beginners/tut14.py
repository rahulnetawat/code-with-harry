# Try Except Exception Handling In Python.

print("Please enter Num1: ")
num1 = input()

print("Please enter Num2: ")
num2 = input()
try:
    print("The sum of 2 numbers: ", int(num1) + int(num2))
except Exception as e:
    print(e)

print("This line is very IMP.")