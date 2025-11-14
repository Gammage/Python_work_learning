##Returning a dictionary##

#a function can return any kind of value you need it to, including more complicated
#data structures like lists and dictionaries

#for eg, the following function takes in parts of a name and returns a dictoinary
#representing a person

def build_person(firstname,lastname):
    """return a dictionary of information about a person"""
    person = {'first':'first_name','last':'last_name'}
    return person

musician = build_person('jimi','hendrix')
print(musician)

#the function build_person takes in the firstname and lastname
#we create a docstring describing the function
#we create a dictionary assigning the parameters to the dict
#we return the dictionary

#we print the musician

def build_person(first_name,last_name,age=None):
    """return a dictionary of info about a person"""
    person = {'first':'first_name','last':'last_name'}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)

#special value none, used when a variable has no specific value to it. think of
#none as a placeholder value
#in conditional tests, none evalutes to test
#if a function call inclues a value for age, that value is stored in the dictionary
#this function always stores a persons name, can also be modified to store
#any other information you want about a person



