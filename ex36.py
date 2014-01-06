from sys import exit, exc_info

CLS = 50 * "\n"

STATE= ["power off", "oxygen off"]

def start_room(died = 0):
    if died == 0:
        print CLS
        print "You are in your room. Your room on the space station epsilon.\
 You have almost finished your tour here. Tomorrow relieve will arrive\
 and you will go home again"
        print "But you do not feel relieved. You are on edge. You feel\
 like something bad is just around the corner"
        print "All of a sudden there is a crash. You are pushed out of\
 your chair and your head hits the bulk head."
        pause()
        print CLS
        print "You open your eyes and look around. The lights have dimmed."
    else:
        print CLS
        print "You open your eyes and look around. You are back in your room.\
 There is a feeling of deja vu, like you have been through this before."
        
    print "\nWhat will you do?"
    print "1) Stay here."
    print "2) Go to the corridor.\n" 
    next = raw_input(">... ")
   
    try:
        if int(next) == 1:
            death("You thought staying put would be safest, but it only postponed\
 the inevitable. With oxygen and power levels being drained you eventually\
 lose consciousness")
        elif int(next) == 2:
            corridor()
        else:
            wrong_choice()
            start_room(died)
    
    except ValueError:
        print "Number please."
    
    except SystemExit:
        print "\nExiting..."
        
    except:
        print "No idea what went wrong: ", exc_info()[0]
        raise


def death(text):
    died = 1
    print CLS
    print text
    print "\nTry again?\n"
    next = raw_input("y/n? ")
    
    if next.lower() == "y":
        start_room(died)
    else:
        exit(0)


def wrong_choice():
    print "\nWrong choice"
    print "\nTry again?\n"
    next = raw_input("y/n? ")
    
    if next.lower() == "y":
        return
    else:
        exit(0)


def corridor():
    print CLS
    print "You leave your room and look around. It is almost as dark as it\
 was back in the room. The only light comes the red emergency lights."
    print "On your right you see the escape pod while in front of you there is\
 the door to engineering"
    
    print "\nWhat will you do?"
    print "1) Go back to your room."
    print "2) Go to the escape pod."
    print "3) Go to engineering.\n"
    next = raw_input(">... ")
    
    try:
        if int(next) == 1:
            death("\nYour room was not the safest choice afterall. With oxygen\
 and power levels being drained you eventually lose consciousness.")
        elif int(next) == 2:
            escape_pod()
        elif int(next) == 3:
            engineering()
        else:
            wrong_choice()
            corridor()
    
    except ValueError:
        print "Number please."
    
    except SystemExit:
        print "\nExiting..."
        
    except:
        print "No idea what went wrong: ", exc_info()[0]
        raise


def escape_pod():
    if STATE[0] == "power":
        power = "green"
    else:
        power = "red"
        
    if STATE[1] == "oxygen":
        oxygen = "green"
    else:
        oxygen = "red"
        
    print CLS
    print "When you aproach the escape pod you notice the status lights."
    print "The power light shows %s and the oxygen light shows %s."\
 % (power, oxygen)
    
    print "\nWhat will you do?"
    print "1) Use the escape pod."
    print "2) Go back to the corridor.\n"
    next = raw_input(">... ")
    
    try:
        if int(next) == 1:
            if STATE[0] == "power" and STATE[1] == "oxygen":
                print CLS
                print "You made it. Thanks to the escape pod you got away from\
 the station. And two days later you were picked up by the ship that was\
 supposed to bring the relieve crew.\n Good Job!"
                pause()
                exit(0)
            else:
                death("You enter the escape pod and using the last remaining\
 power you launch from the station. However without enough power or oxygen you\
 do not make it very far.")
        elif int(next) == 2:
            corridor()
        else:
            wrong_choice()
            escape_pod()
    
    except ValueError:
        print "Number please."
    
    except SystemExit:
        print "\nExiting..."
    
    except:
        print "No idea what went wrong: ", exc_info()[0]
        raise


def engineering(suit = 0, toolkit = 0):
    print CLS
    print "Engineering is a mess. Most controls are damaged and it is defenitly\
 colder here than back in the corridor"
    print "Thankfully you can see the monitor for enviromental and power levels\
 is still working."
    if toolkit == 0:
        print "Turning around you notice a toolkit. That could be quite handy for\
 repairs."
    print "At the back of the room there is the exit to enviromental controls\
 and on the left is the passage that leads to the power conduit."

    print "\nWhat will you do?"    
    print "1) Look at the monitor."
    print "2) Go to enviromental controls."
    print "3) Go to passage."
    if toolkit == 0:
        print "4) Go to back to the corridor."
        print "5) Take the toolkit.\n"
    else:
        print "4) Go to back to the corridor.\n"
    next = raw_input(">... ")
    
    try:
        if int(next) == 1:
            monitor(suit, toolkit)
        elif int(next) == 2:
            enviromental_controls(suit, toolkit)
        elif int(next) == 3:
            passage(suit, toolkit)
        elif int(next) == 4:
            corridor()
        elif int(next) == 5 and toolkit == 0:
            print CLS
            print "You took the toolkit. Smart thinking\n"
            pause()
            toolkit = 1
            engineering (suit, toolkit)
        else:
            wrong_choice()
            engineering(suit, toolkit)
    
    except ValueError:
        print "Number please."
        
    except SystemExit:
        print "\nExiting..."
    
    except:
        print "No idea what went wrong: ", exc_info()[0]
        raise
    

def monitor(suit, toolkit):
    print CLS
    if STATE[0] == "power off" and STATE[1] == "oxygen off":
        print "The monitor shows both the oxygen and the power levels are way\
 below optimal.\n"
    elif STATE[0] == "power" and STATE[1] == "oxygen off":
        print "The monitor shows power levels are nominal but oxygen levels are\
 still below optimal.\n"
    else:
        print "The monitor shows both oxygen and power levels are nominal.\n"
    pause()
    engineering(suit, toolkit)


def pause():
    next = raw_input("\nPress enter to continue.")
    
    if next == True:
        return
 

def enviromental_controls(suit, toolkit):
    print CLS
    if STATE[1] == "oxygen off":
        print "Enviromental controls is in a pretty good state. You use the\
 diagnostic panel and can see the reason for the low oxygen levels."
        print "The air scrubber is not working anymore and needs to be reset."
    else:
        print "You use the diagnostic panel and you can see that the oxygen\
 levels are back to normal."

    if suit == 0:
        print "When you look away from the panel you notice an enviromental\
 suit hanging of the wall."
    
    print "\nWhat will you do?"
    print "1) Go back to engineering."
    if suit == 0:
        print "2) Reset the air scrubber."
        print "3) Take the enviromental suit.\n"
    else:
        print "2) Reset the air scrubber.\n"
        
    next = raw_input(">... ")
    
    try:
        if int(next) == 1:
            engineering(suit, toolkit)
        elif int(next) == 2:
            air_scrubber(suit, toolkit)
        elif int(next) == 3 and suit == 0:
            print "You took the enviromental suit.\n"
            pause()
            suit = 1
            enviromental_controls(suit, toolkit)        
        else:
            wrong_choice()
            enviromental_controls(suit, toolkit)
    
    except ValueError:
        print "Number please."
    
    except SystemExit:
        print "Exiting..."
    
    except:
        print "No idea what went wrong: ", exc_info()[0]
        raise


def passage(suit, toolkit):
    print CLS
    if suit == 0:
        death("You try to use the passage but as soon as you enter you\
 notice you can't breathe. Before you pass out you finally notice the hull is\
 damaged and you can see space through the hole")
    else:
        print "Because of the damage done to the hull you can not savely use\
 the passage. Thankfully you took the enviromental suit with you. You put it\
 on and make it to the power conduit without a problem."
        pause()
        power_conduit(suit, toolkit)


def air_scrubber(suit, toolkit):
    print CLS
    if STATE[0] == "power off":
        print "You try to reset the air scrubber however the diagnostic panel\
 shows there is not enough power."
    else:
        print "You succesfully reset the air scrubber."
        STATE[1] = "oxygen"
    pause()
    enviromental_controls(suit, toolkit)


def power_conduit(suit, toolkit):
    print CLS
    if STATE[0] == "power off":
        print "You arrived at the power conduit and can see the repairs that\
 need to be done."
    else:
        print "The power conduit has been fixed. Power should be restored."

    print "\nWhat will you do?"
    if STATE[0] == "power off":
        print "1) Go back to engineering."
        print "2) Fix the power conduit.\n"
        
    else:
        print "1) Go back to engineering.\n"
    next = raw_input(">... ")
    
    try:
        if  int(next) == 1:
            engineering(suit, toolkit)
        elif int(next) == 2:
            if toolkit == 0:
                print "You do not have the necessary tools. Maybe you should\
 pick up the toolkit in engineering."
            else:
                print "The power conduit is fixed."
                STATE[0] = "power"
                pause()
                power_conduit(suit, toolkit)
        else:
            wrong_choice()
            power_conduit(suit, toolkit)
    
    except ValueError:
        print "Number Please."
    
    except SystemExit:
        print "Exiting..."
    
    except:
        print "No idea what went wrong: ", exc_info()[0]
        raise


start_room()