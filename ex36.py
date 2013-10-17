from sys import exit

def start_room():
    print """You are in your room. Your room on the space station epsilon. 
    You have almost finished your tour here. Tomorrow relieve will arrive 
    and you will return home again"""
    print """But you do not feel relieved. You are on edge. You feel 
    like something bad is just around the corner"""
    print """All of a sudden there is a crash. You are pushed out of
    your chair and you head hits the bulk head."""
    print """You open your eyes and look around. The lights have dimmed.\n"""
        
    print "What will you do?"
    print "Stay here. 1)"
    print "Go to the corridor. 2)\n" 
    next = raw_input(">... ")
   
    if int(next) == 1:
        death()
    elif int(next) == 2:
        corridor()
    else:
        print "Wrong choice"
        exit(0)


def death():
    print "You choose wrongly"
    print "Continue?"
    next = raw_input("y/n? ")
    
    if next.lower() == "y":
        start_room()
    else:
        exit(0)


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
        print "You choose 2"
        #escape_pod()
    elif int(next) == 3:
        print "You choose 3"
        #engineering()
    else:
        print "Wrong choice"
        exit(0)


start_room()