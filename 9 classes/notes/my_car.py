##importing a single class##

#so for importing modules we can use files that represent a class and use docstring eg

# from car_import import Car

#statement above tells python to import the car_import module and the class car
#same functionality, clean main program file and easy to read
#store most of the logic in seperate files
#once your classes work as you want them to, you can leave those files alone
#and focus on higher lvl logic

# from car_import import Car, ElectricCar

# my_leaf = ElectricCar('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())

# my_mustang = Car('ford','mustang',2024)
# print(my_mustang.get_descriptive_name())

##Importing entire module##

# import car_import

#you have to define the module when using it though:

# my_mustang = car_import.Car('ford','mustang',2024)
# print(my_mustang.get_descriptive_name())

##Importing all classes from a module##

# from car_import import *
#book dont like the above. 
    #its helpful to be able to read the top of a file and get a clear sense of which
    #classes a program uses
    #confusion which names in file
    #even though its not recommended people use it so its mentioned in book
    #better off using module_name.classname syntax
    
#importing a module into a module#

#at this point, i have seperated electric car/batter and car in their respective
#files/modules
#see electric_car_import where i have in that module imported car_import

# from car_import import Car
# from electric_car_import import ElectricCar

# my_leaf = ElectricCar('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())

#as the respective imported modules are connected outside this file, they should
#both work in this one. but the classes have to be defined whether when used
#directly or in the from/import statement

#without connecting the two modules, when we reference them here it wouldnt work

#Using aliases

#pretty simple shit
#example of aliases
#simple for not having to type long classnames.
#work for modules and class names imported

# from car_import import Car
# from electric_car_import import ElectricCar as EC

# my_leaf = EC('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())

#for modules:

from car_import import Car
import electric_car_import as ECI

my_leaf = ECI.ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())

#in this example, ive used an alias for the electric_car module.
#the classes in electric_car module are NOT aliased and have to be called as in
#as per the module

#python gives many options on how to structure code in a large project
#good to know all these possibilities so you can structure your project

#keep code simple. try do everything in one file and move classes to seperate
#modules once everything is working
#if you like how modules and files interact, try storing your classes in modules
#when you start a project. find an approach that lets you write code that works
#:)

