# Below function to write. Note this is not appending and data.
# f = open("rahul.txt", "w")

# Below function to append.
f = open("rahul.txt", "a")
a = f.write("This file is created by write file handling.\n")
print(a)
f.close()

# Handling read and write both.
f = open("rahul.txt", "r+")
print(f.readline())
f.write("thank you.")