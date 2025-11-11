#make a dictionary containing three major rivers, and the country each river
#runs through

major_rivers = {'nile':'egypt',
          'trent':'england',
          'danube':'germany',
          'nileasdasd':'george',}

#use a loop to print each sentence about a river
#a loop to print the name of each river
#a loop to print the name of each country included in the dictionary

# for river, country in major_rivers.items():
#     if 'nile' in river:
#         print(f"{river.title()} is in {major_rivers[river]}")
#     if 'trent' in river:
#         print(f"trent sucks d**k")
#     if 'danube' in river:
#         print("a lovely germin river")
        
##the above wouldnt work, because 'nile' doesn't pull exact key

for river, country in major_rivers.items():
    if river == 'nile':
        print(f"{river.title()} is in {major_rivers[river]}")
    if river == 'trent':
        print(f"{river.title()} is a terrible river")
    if river == 'danube':
        print(f"{river.title()} is a river in {major_rivers[river]}")
                
print('\nRivers in dict:')
for river in major_rivers:
    print(river.title())
    
print("\nCountries in the dictionary calling the values")
for countries in major_rivers.values():
    print(countries.title())
    
