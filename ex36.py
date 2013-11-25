from sys import exit

cls = 50 * "\n"


def start_room(died=0):
    if died == 0:
        print cls
        print "You are in your room. Your room on the space station epsilon.\
 You have almost finished your tour here. Tomorrow relieve will arrive\
 and you will return home again"
        print "But you do not feel relieved. You are on edge. You feel\
 like something bad is just around the corner"
        print "All of a sudden there is a crash. You are pushed out of\
 your chair and you head hits the bulk head."
        print "You open your eyes and look around. The lights have dimmed."
    else:
        print cls
        print "You open your eyes and look around. There is a feeling of deja\
 vu, like you have been through this before."
        
    print "\nWhat will you do?"
    print "Stay here. 1)"
    print "Go to the corridor. 2)\n" 
    next = raw_input(">... ")
   
    try:
        if int(next) == 1:
            death("You thought staying put would be safest, but it only postponed\
 the inevitable. With oxygen and power levels being drained you eventually\
 lose consciousness")
        elif int(next) == 2:
            corridor()
        else:
            print "wrong"
            #wrong_choice(start_room(died))
    except:
        print "wrong input"
        exit(0)


def death(text):
    died = 1
    print cls
    print text
    print "\nTry again?"
    next = raw_input("y/n? ")
    
    if next.lower() == "y":
        start_room(died)
    else:
        exit(0)


def wrong_choice(location):
    print "\nWrong choice"
    print "\nTry again?"
    next = raw_input("y/n? ")
    
    if next.lower() == "y":
        location
    


def corridor():
    print "You leave your room and look around. You notice it is as dark as it\
 was back in the room. The only light comes the red emergency lights."
    print "On your right you see the escape pod while in front of you there is\
 the door to engineering"
    
    print "\nWhat will you do?"
    print "Go back to your room. 1)"
    print "Go to the escape pod. 2)"
    print "Go to engineering. 3)"
    next = raw_input(">... ")
    
    if int(next) == 1:
        death()
    elif int(next) == 2:
        escape_pod()
    elif int(next) == 3:
        engineering()
    else:
        wrong_choice()


def escape_pod():
    print "When you aproach the escape pod you notice the status lights."
    print "It doesn't bode well. Both the oxygen and power lights are red\
 and blinking."
    
    print "\nWhat will you do?"
    print "Use the escape pod. 1)"
    print "Go back to the corridor. 2)"
    next = raw_input(">... ")
    
    if int(next) == 1:
        death()
    elif int(next) == 2:
        corridor()
    else:
        wrong_choice()


def engineering():
    print "Engineering is a mess. Most controls are damaged and it is defenitly\
 colder here than back in the corridor"
    print "Thankfully you can see the monitor for enviromental and power levels\
 is still working"
    print "Turning around you notice a toolkit. That could be quite handy for\
 repairs."
    print "At the back of the room there is the exit to enviromental controls\
 and on the left is the passage that leads to the power conduit."

    print "\nWhat will you do?"    
    print "Look at the monitor. 1)"
    print "Take toolkit. 2)"
    print "Go to enviromental controls. 3)"
    print "Go to passage. 4)"
    print "Go to back to the corridor. 5)"
    next = raw_input(">... ")
    
    if int(next) == 1:
        monitor()
    elif int(next) == 2:
        toolkit()
    elif int(next) == 3:
        enviromental_controls()
    elif int(next) == 4:
        passage()
    elif int(next) == 5:
        corridor()
    else:
        wrong_choice()
    

def monitor():
    print "The monitor shows both the oxygen and the power levels are way below\
 optimal\n"
    engineering()


def toolkit():
    print "You took the toolkit\n"
    engineering()


def enviromental_controls():
    print "Enviromental controls is in a pretty good state. You use the\
 diagnostic panel and can see the reason for the low oxygen levels"
    print "The air scrubber is not working anymore and needs to be reset"
    print "When you look away from the panel you notice an enviromental suit\
 hanging of the wall"
    
    print "\nWhat will you do?"
    print "Reset the air scrubber. 1)"
    print "Take the enviromental suit. 2)"
    print "Go back to engineering. 3)"
    next = raw_input(">... ")
    
    if int(next) == 1:
        air_scrubber()
    elif int(next) == 2:
        print "You took the enviromental suit\n"
        enviromental_controls()
    elif int(next) == 3:
        engineering()
    else:
        wrong_choice()


def air_scrubber():
    print "You try to reset the air scrubber however the diagnostic panel shows\
 there is not enough power\n"
    enviromental_controls()


def passage():
    print "You try to use the passage but as soon as you enter you notice you\
 can't breathe. Before you pass out you finally notice the hull is damaged and\
 you can see space through the hole"
    death()


def power_conduit():
    print "You arrived at the power conduit and can see the repairs that need\
 to be done."

    print "\nWhat will you do?"
    print "Fix the power conduit. 1)"
    print "Go back to engineering. 2)"
    next = raw_input(">... ")
    
    if int(next) == 1:
        print "The power conduit is fixed. Power should be restored."
    elif int(next) == 2:
        engineering()


start_room()