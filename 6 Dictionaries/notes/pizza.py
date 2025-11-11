##A LIST IN A DICTIONARY##
#sometimes useful to put a list inside a dictionary
    #eg, consider how you might describe a pizza that someone is ordering
    
#store information about a pizza being ordered
pizza = {'crust':'thick',
         'toppings': ['mushrooms','extra cheese']
         }

#you can store a list as a value in key:value pair. see above

#summarise order
print(f"you ordered a {pizza['crust']}-crust pizza"
      " with the following topics")

for topping in pizza['toppings']:
    print(f'{topping}')
    
#create a for loop in pizza key toppings list
#print the topping item(s)(all the list items for toppings)

#when using print, you can combine strings with a series of """"

#you can nest a list inside the dictionary anytime you want more then one value
#to be associated with a single key in the dictionary.in the favourite languages,
#we could create more then one favourite language per person

#see favourite_languages for further example in nested lists in dictionaries