#Creating Dictionery
myword = {"centos": "Open source server distribution.",
        "ubuntu": "Open source desktop distribution",
        "redhat": "Propriatory OS.",
        "arch": "Open Source desktop and client distribution."
        }
#Printing all keys of dictionery
print(myword.keys())
print("Check Keys name from above line.")
print("Enter your choice name:", end='')
#take input from user to print element of dictionery.
tia1 = input()
#use of get functio to access element of dictionery.
print(myword.get(tia1,"No Such Key exist in dictionery"))
#print(myword[tia1])
