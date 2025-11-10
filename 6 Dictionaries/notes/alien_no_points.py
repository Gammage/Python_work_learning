##USING GET() TO ACCESS VALUES##

#using keys in square brackets to retrieve the value your interested in from a
#dicionary may cause a potential problem: if they key doesn't exist you'll get
#an error

alien_0 = {'color':'green','speed':'slow'}
# print(alien_0['points'])

#this provides a keyerror: 'points'

#more error handling in chapter 10

#for dictionaries specifically, you can use the get() method to set a default
#value that will be returned if the requested key doesn't exist

#the get() method requires a key as a first argument. As a second optional
#argument, you can pass the value to be returned if the key doesnt exist

point_value = alien_0.get('points','no point value assigned')
print(point_value)

#if you leave the second value out 'no point vlaue assigned' python returns
#'none'. the special value means "no value exists". this is not an error.
#its a special value meant to indicate the absence of a value

##if key 'points' exists in the dictionary, you'll get the corresponding value.
#if it doesnt, you get the default value. in this case, points doesnt exist.
#we get a clean message instead of an error

