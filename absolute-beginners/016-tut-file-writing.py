# File writing tutorial.

f = open("file-io-test.txt", "r")
#############################################
# Practise 1
# In this practise we can saw the output of
# the whole file.
#
# content = f.read()
# print(content)
#############################################

#############################################
# Practise 2
# # First 3 words printing.
# content = f.read(3)
# print(content)
#
# # Next 3 words printing after 1st read.
# content = f.read(3)
# print(content)
#############################################

#############################################
# Practise 3
# content = f.read(255)
# print("1", content)
#
# content = f.read(255)
# print("2", content)
#############################################

#############################################
# Printing file character via For Loop.
# for line in f:
#     print(line, end="")
# Note: end="" in removing blank line from the
# FOR LOOP.
#############################################

#############################################
# Printing via f.readline function.
print("1.", f.readline(),end="")
print("2.", f.readline(),end="")
#############################################
f.close()