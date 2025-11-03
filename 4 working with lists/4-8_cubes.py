#number raised to the third power is called a cube. 

# cubed = list(range(1,11))
# for value in cubed:
#     value = value**3
#     print(value)
    
# cubed = list(range(1,11))

cubed = [value**3 for value in range(1,11)]
print(cubed)
#you dont need to define list word, [] is a list?
#gpt confirmed it is, so dont need list when [] in play