#Define the Dictionary
myword = {"centos": "Open source server distribution.",
        "ubuntu": "Open source desktop distribution",
        "redhat": "Propriatory OS.",
        "arch": "Open Source desktop and client distribution."
        }
#print all the keys of Dictionary
print(myword.keys())
print("Check Keys name from above line.")
print("Enter your choice name:", end='')
#To take an input from the user
tia1 = input()
#print the Dictionary Value according to the keys as an input
print(myword[tia1])
