#can also test to see if 2 numbers arent equal. eg;

answer = 17
if answer != 23:
    print("that isn't the correct answer")
    
#the answer 17 is not equal to 23, therefore the if statement is true, using
#the not equal to operator !=

#you can use other things too, such as:

age = 19
age < 21
# true 19 is less than 21

age <= 21
#still true. less than OR equal to

age > 21
#false. 19 isnt more than 21

age >= 21
#false. 19 isnt greater or equal to 21

# these can be used as part of if statement

if age <= 21:
    print('no.')
    
#when checking multiple conditions we can use and

age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >= 21
#false. age_0 is greater than or equal to 21, and age_1 is NOT greater or equal to
#21. therefore this is false. both conditions need to be true

###AND CONDITIONAL###
age_1 = 22
age_0 >= 21 and age_1 >= 21
#true. age_0 is greater than 21 and age_1 is greater than 21

#you can use parentheses around individual tests but not required
    #I will use paranthesis. it makes it much easier to read.
    
(age_0 >= 21) and (age_1 >= 21)

###OR CONDITIONAL##
age_0 = 22
age_1 = 18

(age_0 >= 21) or (age_1 >= 21)
#true. age_0 is greater or equal to 21, age_1 is Not greater or equal to 21.
#therefore as one of the conditions is met is is true, in a OR conditional

age_0 = 18
(age_0 >= 21) or (age_1 >= 21)
#false. age_0 is NOT greater or equal to 21. age_1 is NOT greater or equal to 21.
#both conditionals are not met.


