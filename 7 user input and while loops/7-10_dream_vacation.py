##dream vacation exercise##
#write a program that polls users about their dream vacation.
#write a prompt similiar to if you could visit one place in the world, where
#would you go?

vacation_poll = {}

poll_active = True

while poll_active:
    name = input("what is your name?")
    dream_place = input("what is your dream place?")
    
    vacation_poll[name] = dream_place
    
    repeat = input("Does anyone else wish to enter the poll? (yes/no)")
    if repeat == "no":
        poll_active = False
        
for name, place in vacation_poll.items():
    print(f"{name} favourite place is {place}")
            
