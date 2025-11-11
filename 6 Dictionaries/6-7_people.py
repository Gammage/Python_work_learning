##People exercise 6-7##
#start with program you wrote for exercise one
#make two new dictionaries representing different people
    #store all three dictinoaries in a list called people
    #loop through list of people
    #as you loop through the list, print everything you know about each person
    
bobsmith = {'name':'bob',
         'last name':'smith',
         'age':30,
         'city':'glasgow',}

gamminator = {'name':'ben',
              'last name':'gammage',
              'age':34,
              'city':'leicester',}

knobrob = {'name':'rob',
           'last name':'loveland',
           'age':33,
           'city':'bournemouth',}

people = [bobsmith,gamminator,knobrob,]

for index, person in enumerate(people):
    print(f"\nUser: {index}")
    full_name = f"{person['name']} {person['last name']}"
    print(f"Name: {full_name.title()}")
    print(f'Age: {person['age']}')
    print(f"Location: {person['city']}")

#items() only works on dictionariers not list
#cant reference the list item as its stored by index numbers, not keys.
#so you can only reference its position
#enumerate() gives me both the index number and item(each dictionary in this case)


