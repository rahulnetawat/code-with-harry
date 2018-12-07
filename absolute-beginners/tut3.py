# String Slicing And Other Functions

mystr = "python is very vast language."

print(len(mystr)) #Printing string of mystr variable.

print(mystr[0:6]) # String slicing example: Means we want to print selected value instead of whole value of variable.

print(mystr.count("vast"))# Printing word or character count.

print(mystr[0:6:2]) # We are skipping every 2nd value of the output.

print(mystr[::3]) # We are skipping here every 3rd value of the output from the whole string.

print(mystr[::-3]) # Here we getting output in reverse order.

print(mystr.isalnum()) # We are getting False value bcz spaces present in script.

print(mystr.isalpha()) # We are getting False value again due to spaces in script.

print(mystr.endswith("language.")) # Strings need to be exact, otherwise we are going to get output in False.

print(mystr.count("vast")) # We are counting the string value or alphabet repeated in variable.

print(mystr.capitalize()) # This function is capitalize the first alphabet of the character.

print(mystr.find("very")) # This fuction is searching the string value and printing the list number output.

print(mystr.lower()) # Converting all values in lower case.

print(mystr.upper()) # Converting all values in upper case or block letters.

print(mystr.replace("very", "a")) # We are replacing the particular string with own written value.