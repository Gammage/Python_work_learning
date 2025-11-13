##using a break to exit a loop##
#to exit a while loop immediately without running any remaining code in the loop
#regardless of the results of any conditional test, use the break statement
    #the break statement directs flow of program
        #use it to control which lines of code are execuded which aren't,
        #so the program only executes code you want it to, when you want it to

#consider a program that asks the user about places they've visited.
#we can stop the while loop in this program by calling break as soon as the user
#enters the quit value

prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(enter quit when you have finished)"

while True:
    city = input(prompt)
    
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
#a loop that starts with while true will run forever unless it reaches a break statement
#you can use break statement in any of pythons loops. for example, you could use
#break to quit a for loop thats working through a list or dictionary

