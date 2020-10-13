while(True):        #this will run the program continuously until you break it
        a=input=int(("enter your choice 1 or 0"))
        if a==1:

                myword = {"centos": "Open source server distribution.",
                        "ubuntu": "Open source desktop distribution",
                        "redhat": "Propriatory OS.",
                        "arch": "Open Source desktop and client distribution."
                        }
                print(myword.keys())
                print("Check Keys name from above line.")
                print("Enter your choice name:", end='')
                tia1 = input()
                print(myword[tia1])
         else :
                print("your choice")
                break
