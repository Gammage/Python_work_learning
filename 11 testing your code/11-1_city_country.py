##City country exercise##
#write a function that accepts two parameters a city name and a country name
#the function should return a single string of the form city, country such as
#london, england. 

#store the function in a module called city_functions.py
#save this file in a new folder so pytest wont try to run the tests we've already
#written

from city_functions import city_country

while True:
        city = input("what is your city?")
        if city == 'q':
            break
        country = input("what is your country?")
        if country == 'q':
            break

formatted_city_country = city_country(city,country)
print(formatted_city_country)