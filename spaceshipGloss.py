import time
shipName = "Gloss"
captain = "Captain Joon "
location = "Andromeda Galaxy"
password = "Syubie"

pAttempt = input("Enter the password: ")
while pAttempt != password:
    print ("Password incorrect")
    pAttempt = input("Enter the password: ")
print ("Password correct. Welcome to " + shipName)

print ("")
print ("The spaceship " + shipName + " is currently visiting " + location + ".")

choice = ""
while choice != "/exit":
    print ("What would you like to do, " + captain + "?")
    print ("")
    print ("a. Travel to another galaxy")
    print ("b. Fire thrusters")
    print ("c. Open the airlock")
    print ("d. Self-destruct")
    print ("/exit to exit")
    print ("")
    choice = input ("Enter your choice: ")
    if choice == "a":
        destination = input("Where would you like to go? ")
        print ("Leaving " + location)
        print ("Travelling to " + destination)
        #time.sleep(5))
        print("Arrived at " + destination)
        location = destination
    elif choice == "b":
        print ("Firing thrusters")
        #time.sleep(1))
        print ("BANG(ya)")
        #time.sleep(1))

    elif choice == "c":
        print ("Opening airlock")
        #time.sleep(3))
        print ("Airlock open")
        #time.sleep(1))

    elif choice == "d":
        confirm = input("Are you sure you want " + shipName + "to self-destruct? (y/n)")
        if confirm == "y":
            print (shipName + " will self-destruct in")
            print ("3")
            #time.sleep(1)
            print ("2")
            #time.sleep(1)
            print ("1")
            #time.sleep(1)
            print ("Goodbye")
            print ("BOOM")
            choice = "/exit"

    elif choice == "/exit":
        print ("Goodbye")

else:
    print ("Invalid input. Please select a, b, c or d. /exit to exit")
