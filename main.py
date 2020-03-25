# This a program for a command line friend for those who wants to tell many things but can not say because of loneliness


class chatBot():
    """This is a class which wraps whole functions in it."""

    __contact = {'avinash': '6266390748'}  # Private Dictionary of contacts so that it can not be accessed outisde the class
    def Intro(self):
        """This function is the introduction of this commandline chatbot."""
        print("Hello, there!")
        print("I am your new digital friend as I don't like noise pollution, I only types ",end=';)\n')
        print("But I am always here for you to chat with you and listen to you as I love to listen people.")
        print("Type in help for commands you can use with me.")

    def showContacts(self,name):
        """This function will check whether the name is already in keys list of contact dictionary or not if it esists it will show otherwise ask to add temorarily."""
        if name in self.__contact.keys(): # Check key is availabe or not
            print(f"Contact of {name} is {self.__contact.get(name)}")

        else:
            print("It is not in my contact list!!!\nWould you like to add it? ")
            op = input("Y/N: ").lower() # To make letters in lowercase to avoid case sensitivity
            if op=='y':
                contNum = input("Please enter the contact number: ")
                self.__contact[name] = contNum # Adding new entry to contact dictionary
                print("Done bhai!!!")
                print("I will remember it untill you close me. I know am little dumb!!!")

            elif 'n' in op:
                print("Ohk, No problm!!!")

            else:
                print("Please input a valid option Bro!!!")

    def help(self):
        """This lists the basic commands of this program."""
        print("\n*******************HELP*******************")
        print("Hello\t\t\t\t\tFor basic interaction")
        print("Contact of\t\t\t\tTo display contact number of person you have added alredy (By default it has only creators contact)")
        print("List contacts\t\t\tTo display name of contacts saved.")
        print("Help or list commands   To display basic command can use with me")
        print("Bye\t\t\t\t\t\tFor exiting out of program")

    def listContacts(self):
        print(self.__contact.keys())

objBot = chatBot() # Object of the class chatBot to access it's members and methods
objBot.Intro() # Function Call of introduction
while 1: # Infinite loop so that it will iterarte itself until we does not want to stop it.
    command = input(">>> ").lower()
    if 'hello' in command:
        print("Oh, Can I know your good name???")
        name = input(">>>")
        print(f"Hello {name}, Nice name. How are you???")
        reply = input(">>>").lower()
        if 'nice' in reply or 'great' in reply or 'fine' in reply:
            print("Great!!!")
            if 'you' in reply:
                print("As always, The Best!!!")

        else:
            print("What happend? You can tell me, if you want")
            prblm = input(">>>")

            with open("problems.txt", "a") as file: # To store problems so that we can resolve them later
                file.write(f"{name}: {prblm}")
            print("Don't Worry!!! Every thing will be great, just be happy")

    elif 'list contacts' in command:
        objBot.listContacts()

    elif 'contact' in command:
        name = command.replace('contact of ',"")
        objBot.showContacts(name)


    elif 'help' in command or 'list commands' in command:
        objBot.help()

    elif 'bye' in command:
        print("Do you want to give me any feed back!!!")
        op = input("Y/N: ").lower()

        if 'y' in op:
            print("Great! So, please enter your name first:")
            name = input(">>>")
            print("Ohk, Now you can give feedback:")
            feed = input(">>>")

            with open("feedback.txt") as file:
                file.write(f"{name}: {feed}")
            print("Thank You!!!")

        elif 'n' in op:
            print("Ohk, No problm!!!")

        else:
            print("Please input a valid option Bro!!!")

        break