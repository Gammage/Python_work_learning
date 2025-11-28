##11-2population exercise##
#modify your function so it requires a third parameter, population
#it should now return a single string of the form city, country, population
#run the test again, make sure test_city_country() fails
#modify the function so the population parameter is optional.
#run the test, make sure test_city_country() passes again

#write a second test called test_city_country_population() that verifies you can
#call your function with the values 'santiago','chile'and'population=5000_000'
#run the test one more time, make sure this new test passes.

from city_functions import city_country

while True:
        city = input("what is your city?")
        if city == 'q':
            break
        country = input("what is your country?")
        if country == 'q':
            break
        population = input(f"what is the population of {city}")
        if population == 'q':
            break
        
        print(f"information to submit {city},{country},{population}")
        if population:
            formatted_city_country = city_country(city,country,population)
        else:
            formatted_city_country = city_country(city,country)
        

# formatted_city_country = city_country(city,country,population='')
# print(formatted_city_country)

