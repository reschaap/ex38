# as example only 
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
        print "You choose 2"
    else:
        print "Wrong choice"
    
    exit(0)
        

def death():
    print "death"
    exit(0)

start_room()
        
