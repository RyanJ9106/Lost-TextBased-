import time
import sys

print("Hello and Welcome to Lost")
input("Press enter to Wake Up: ")

#Variables
ball = False
clue1 = False
flashlight = False
covereddoor = False

#########################################################################################################################################################

#Functions
def room0s():
    firstrooms = input("\nYou have woken up in a dimly lit room and have no idea where you are. You see lights seeping through gaps in the wall, you realise the gaps are the outlines of doors. You can either go left (1) or right (2). (1 or 2): ")

    if firstrooms == "1":
        room1()
        
    if firstrooms == "2":
        room2()

#########################################################################################################################################################

def room0():
    firstroom = input("\nYou are back in the starting room where you awoke, will you go left (1) or right (2)? (1 or 2): ")

    if firstroom == "1":
        room1()
        
    if firstroom == "2" and flashlight == True:
        room2f()
    
    elif firstroom == "2":
        room2()

#########################################################################################################################################################

def room1():
    global ball 
    global clue1

    secondroom = input("\nYou see a crack in the wall (1) and a table in the corner (2) (or back (3)). (1 or 2 or 3): ")

    if secondroom == "2":
        pickup = input("\nThere is a small box of balls on the table and you pick one up. (1 to turn back.): ")
        ball = True

        if pickup == "1":
            room1()

    if secondroom == "1":
        wallcrack = input("\nThe inspect the crack in the wall and there seems to be an endless void through the otheside of the wall. Throw something through the crack (1) or go back to the centre of the room (2)? (1 or 2): ")
        
        if wallcrack == "1" and ball == True:
            throw = input("\nYou through the ball through the wall and it seems to just float away (Clue 1 Found). (1 to turn back.): ")
            clue1 = True
            ball = False

            if throw == "1":
                room1()

        else:
            noitem = input("\nYou have nothing to through through the wall. (1 to turn back.): ")

            if noitem == "1":
                room1()

        if wallcrack == "2":
            room1()
    
    if secondroom == "3":
        room0()

#########################################################################################################################################################

def room2():
    global ball 
    global clue1
    global flashlight

    thirdroom = input("\nYou enter a pitch black room and hear a creaking noise from the corner, you cant see what it is. There is a flashlight on the floor but its in direction of the creeking.\nWill you, Try and grab flashlight (1) or inspect the creaking in the corner (2) (or go back (3)). (1 or 2 or 3): ")

    if thirdroom == "1":
        Death1 = input("\nYou scamble for the flashlight and try to grab it, your arm gets ripped off by the creature in the corner. You bleed to death. (Press R to Restart): ")

        if Death1 == "R":
            room0()

    if thirdroom == "2" and ball == True:
        Throw = input("\nYou slowly creep towards the corner and you see the outline of a creature. You can either turn back now (1) or keep going towards the creature (2) or throw your ball at to the creature (3). (1 or 2 or 3): ")

        if Throw == "1":
            room2()
        
        if Throw == "2":
            Death2 = input("\nYou go further into the darkness and the creature tears both of your legs off, twisting and pulling them. You bleed to death. (Press R to Restart): ")

            if Death2 == "R":
                room0()
        
        if Throw == "3":
            Friend = input("\nYou throw your ball towards the creature and the creature passes you the flashlight and plays with the ball, you seem to have made friends with the creature. He seems to now be occupied with the ball, leave the room and come back to see if you can talk to him. (1 to turn back): ")
            flashlight = True
            ball = False

            if Friend == "1":
                room0()

    else:
        Creep = input("\nYou slowly creep towards the corner and you see the outline of a creature. You can either turn back now (1) or keep going towards the creature (2). (1 or 2): ")

        if Creep == "1":
            room2()
        
        if Creep == "2":
            Death2 = input("\nYou go further into the darkness and the creature tears both of your legs off, twisting and pulling them. You bleed to death. (Press R to Restart): ")

            if Death2 == "R":
                room0()
    
    if thirdroom == "3":
        room0()

#########################################################################################################################################################

def room2f():
    global clue1
    global covereddoor

    if covereddoor == True:
        dooruncovered = input("\nThere is a door in the corner with the creature playing next to it, will you try and speak to the creature (1) or go through the door (2) (or turn back (3)) (1 or 2 or 3): ")

        if dooruncovered == "1":
            busy = input("\nThe creature is too busy to talk, hes playing with his ball. (1 to turn back.): ")

            if busy == "1":
                room2f()

        if dooruncovered == "2":
            room3()

        if dooruncovered == "3":
            room0()

    else:
        friend = input("\nYou enter the pitch black room, you can see your friend in the corner. Will you speak to your friend (1) or will you turn back (2). (1 or 2): ")

        if friend == "1" and clue1 == True:
            speach1 = input("\nYou speak to the creature and he tells you he is sitting in front of the door into the next room. He asks whether you know any information, you tell him about the crack in the wall and what happens when you threw something through it. He thanks you and moves out of the way and continues to play with his ball. (1 to turn back): ")
            
            if speach1 == "1":
                covereddoor = True
                room2f()

        if friend == "1":
            speach2 = input("\nYou speak to the creature and he tells you he is sitting in front of the door into the next room. He says he wont let you through unless you have found out some information for him (find Clue 1). (1 to turn back): ")

            if speach2 == "1":
                room0()
    


        if friend == "2":
            room0()

#########################################################################################################################################################

def room3():
    space = input("\nYou walk into this room, the ceiling has caved in, and the door locks behind you. You cant leave. You realise the other side of the ceiling is the same as the crack in the wall, you realise you are in a room in space.\nThere are two doors one with darkness behing it (1) and other with a red light (2). (1 or 2): ")

    if space == "1":
        doorlight = input("\nYou shine your light onto the door and realise there are engravings of planets and theories of space all over it. You slowly open the door and the door gets ripped off of its hinges flying out of the room into the endless void, you grab onto the door frame trying to latch on to survive. Your grip slips and you fly out of door. Floating in space forever... (Press R to restart): ")

        if doorlight == "R":
            room0()

    if space == "2":
        twodoor = input("\nYou approach the door with the red light shining out of it, you realise there are no door handles on the door. You kick the door open and see a computer screen with a red light emmiting from it. (Press 1): ")

        if twodoor == "1":
            computer()

def computer():
    passscreen = input("\nYou read the note on the desk it says 'Password: 52852'. Enter the password into the computer: ")
    text = "YOU ARE TRAPPED, FLOATING IN SPACE"
    dot = "................................"

    if passscreen == "52852":
        input("\nThe computer screen has single file in the middle of the screen. (Press Enter to open the file): ")

    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(.25)
    
    for char in dot:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(.5)

    time.sleep(10)
    print("\nThank you for playing lost, hope you enjoyed this short experince.")

#########################################################################################################################################################
    
room0s()
