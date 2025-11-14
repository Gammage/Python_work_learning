##exercise 8-6 city names##
#write a function called city_country() that takes in the name of city
#and country
#call your function with at least three city-country pairs, and print the values
#that are returned

def city_country(city,country):
    """takes in the name of city and country"""
    
    city_info = {'city name':city.title(),'country name':country.title()}
    return city_info

city_data1 = city_country('london','england')
city_data2 = city_country('glasgow','scotland')
city_data3 = city_country('tokyo','japan')


print(city_data1,city_data2,city_data3,sep='\n')