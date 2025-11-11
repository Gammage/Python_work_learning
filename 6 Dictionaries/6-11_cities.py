##city exercise
#make a dictionary called cities
#use the names of three cities as keys in your dictionary
#create a dictionary of information about each city and include:
    #country that city is in
    #approx population
    #one fact about city
#keys for each city dictinoary should be country population, fact
#print name of each city and all the information stored about it

cities = {
    'london': {
        'country':'england',
        'population':3_000_000,
        'fact':'30 crimes per 1000 people',
        },
    'edinburgh':{
        'country':'scotland',
        'population':100_000,
        'fact':'very accessible via walking',
        },
    'leicester':{
        'country':'england',
        'population':500_000,
        'fact':'highest percenatage of non speaking english in a english city',
        },
}

for city_name, facts in cities.items():
    print(f"\nFor {city_name.title()}:")
    print(f"The city is in {facts['country']}")
    print(f"The population is {facts['population']}")
    print(f"A random fact about {city_name.title()}: {facts['fact']}")
    
