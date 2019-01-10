# For loops in Python.

# list1 = ["Rahul", "Dheeraj", "Avinash", "Tia"]
# list1 = ("Rahul", "Dheeraj", "Avinash", "Tia")
# list1 = [ ["Rahul", 1], ["Dheeraj", 2], ["Avinash", 3], ["Tia", 4] ]
# for item in list1:
#     print(item)

# dict1 = dict(list1)
# print(dict1)

# for item, rank in dict1.items():
#     print(item,"rank is", rank)

# for item in dict1:
#     print(item)

items = [int, float, "Rahul", 26, 45, 54, 78, 74, 3, 5]

for item in items:
    if str(item).isnumeric() and item >= 3:
        print(item)