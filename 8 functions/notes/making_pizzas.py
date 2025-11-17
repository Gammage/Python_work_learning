##EXAMPLE OF IMPORTING A FUNCTION##

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(200, 'mushrooms','a shit ton of cheese','BACON')

##when python reads this file, the line import pizza tells python to open/read
#pizza.py and copy all the functions from it into this progrma
#any function defined in pizza will be now available here

#to call a function from an imported module, simple call the module and the specific
#function. call the function with a dot like above example
#this code produces the same output as the original program that didnt import a module

#so it would go like this:
#module_name.function_name()

##IMPORTING SPECIFIC FUNCTIONS##
#you can also import specific functions like so:
#from module_name import function_name
#eg

from pizza import make_pizza

#this can be done for multiple functions

#from module import function_one, function_two,

#when calling a function directly like this, you don't need to use the dot when
#you call a function - we have already explicited imported the function make_pizza

##USING as TO GIVE A FUNCTION ON ALIAS##

#if the name of a function is conflicting with a current one, or its long, you can
#use an alias

#in this example, the function make_pizza() has an alias, mp():

from pizza import make_pizza as mp

mp(8,'chicken')

#we renamed the function from pizza to mp in this program

#general syntax for providing an alias is:
# from module_name import function_name as fn

##Using as to give a module an alias
#you can also give a module an alias
#see below eg

import pizza as p

p.make_pizza(15,'pepperoni')

#all functions from module retain their original names even when module given alias

#general syntax for this approach:
# import module_name as mn


#IMPORTING ALL FUNCTIONS IN A MODULE#
#you can tell python to import every function in a module by using the asterisk 
#operator (*)

from pizza import *

make_pizza(7,'pepperoni')

#as every function is imported using asterisk, you can reference them without dot
#annotation

#its best not to use this approach when working on larger files/ones you didnt write
#if module names have the same as your project, conflicting results will occur
#-best approach is to import the function or functions you want
#or import the entire module and use the dot notation. clear code, easy to read


