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
        wrong_choice()


def death():
    print "Oops!"
    print "Try again?"
    next = raw_input("y/n? ")
    
    if next.lower() == "y":
        start_room()
    else:
        exit(0)


def wrong_choice():
    print "Wrong choice"
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
        escape_pod()
    elif int(next) == 3:
        print "You choose 3"
        #engineering()
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
    print "You can see the panels for monitoring enviromental and power levels"
    print "Both oxygen and power levels show up in the red"
    print "Turning around you notice toolkit. That could be quite handy for\
 repairs"
    print "
    
    print "\nWhat will you do?"
    print "Go to enviromental controls. 1)"
    print "Go to 
    
start_room()