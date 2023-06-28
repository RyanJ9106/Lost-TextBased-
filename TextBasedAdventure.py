print("Hello and Welcome to this text based adventure!")
input("Press enter to Start!")

#Variables
ball = False
clue1 = False
flashlight = False

#Functions
def room0():
    firstRoom = input("\nWelcome to the start of your adventure. You have woken up in a dimly lit room and have no idea where you are. You see lights seeping through gaps in the wall, you realise the gaps are the outlines of doors. You can either go left or right (1 or 2): ")

    if firstRoom == "1":
        room1()
        
    if firstRoom == "2":
        room2()

def room1():
    global ball 

    secondroom = input("\nYou see a crack in the wall (1) and a table in the corner (2) (or back (3)). (1 or 2 or 3): ")

    if secondroom == "2":
        print("\nThere is a small box of balls on the table and you pick one up.")
        ball = True
        room0()

    if secondroom == "1":
        wallcrack = input("\nThe inspect the crack in the wall and there seems to be an endless void through the otheside of the wall. Throw something through the crack (1) or go back to the centre of the room (2)? (1 or 2): ")
        
        if wallcrack == "1" and ball == True:
            print("\nYou through the ball through the wall and it seems to just float away.")
            clue1 = True
            room1()
        else:
            print("\nYou have nothing to through through the wall.")
            room1()

        if wallcrack == "2":
            room1()
    
    if secondroom == "3":
        room0()

def room2():
    global ball 
    global clue1

    thirdroom = input("\nYou enter a pitch black room and hear a creaking noise from the corner, you cant see what it is. There is a flashlight on the floor but its in direction of the creeking.\nWill you, Try and grab flashlight (1) or inspect the creaking in the corner (2) (or go back (3)). (1 or 2 or 3)")

    if thirdroom == "1":
        Death1 = input("\nYou scamble for the flashlight and try to grab it, your arm gets ripped off by the creature in the corner. You bleed to death. (Press R to Restart)")

        if Death1 == "R":
            room0()

    if thirdroom == "2" and ball == True:
        Throw = input("\nYou slowly creep towards the corner and you see the outline of a creature. You can either turn back now (1) or keep going towards the creature (2) or throw your ball at to the creature. (1 or 2)")

        if Throw == "1":
            room2()
        
        if Throw == "2":
            Death2 = input("\nYou go further into the darkness and the creature tears both of your legs off, twisting and pulling them. You bleed to death. (Press R to Restart)")

            if Death2 == "R":
                room0()
        
        if Throw == "3":
            Friend = input("\nYou throw your ball towards the creature and the creature passes you the flashlight and plays with the ball, you seem to have made friends with the creature.")
            flashlight = True
            ball = False

    else:
        Creep = input("\nYou slowly creep towards the corner and you see the outline of a creature. You can either turn back now (1) or keep going towards the creature (2). (1 or 2)")

        if Creep == "1":
            room2()
        
        if Creep == "2":
            Death2 = input("\nYou go further into the darkness and the creature tears both of your legs off, twisting and pulling them. You bleed to death. (Press R to Restart)")

            if Death2 == "R":
                room0()
    
    if thirdroom == "3":
        room0()

room0()