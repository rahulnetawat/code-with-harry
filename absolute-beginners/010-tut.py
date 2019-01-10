# break and continue statement.

i = 0

# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#
#     print(i + 1, end=" ")
#     if (i==50):
#         break
#     i = i + 1
while(True):
    inp = int(input("Enter a number: "))
    if inp>100:
        print("Congratulations, You entered a number greater than 100.")
        break
    else:
        print("Try again.\n")
        continue
        # i = i + 1
