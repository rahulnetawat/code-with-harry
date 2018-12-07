# Lists and Lists Functions.
laptop = ["ram", "battery", "hdd", "led", "wifi", "mouse", 227]

print(laptop[5])

numbers = [2, 8, 9, 11, 67, 7]
# print(numbers[4])
# numbers.sort()    # Sort and reverse may change the original list parameter. Here we are using numbers name list.
# numbers.reverse()

print(numbers[1:4]) # We are getting output in list. Slicing also working here.

# print(max(numbers)) # To print maximum number value from list.
# print(min(numbers)) # To print lowest number value from list.
# numbers = []
# # Using .append function.
# numbers.append('10')
# numbers.append('02')
# numbers.append('1987')
# print(numbers) # In print we are getting our new value which is added.

# Using .insert function to replace index value.
# numbers.insert(1, 54) # On Index number 1 we are replacing existing value with 54 which is given in this example.
# numbers.insert(2, 74)
# numbers.insert(3, 78)
# print(numbers)

# numbers.remove(67) # Here we are removing number 67 from numbers list.
# numbers.pop()  # .pop is removing last index value.
# numbers.pop(1) # Using .pop we are removing number by Index number.
# print(numbers)

# Now using TUPLE. Tuples are immutable.
# numbers[1] = 227
# print(numbers)

# tp = (1, 2, 3)
# # print(type(tp))
# print(tp)

# Number Swwapping example
a = 1
b = 2
a, b = b, a
print(a, b)