##exercise cars 8-14##
#write a function that stores info about a car in a dictionary
#function should always recieve a  manufacturer and model name
#it should accept an arbitrary number of keyword arguments
#call the function with the required information and two other name-value pairs
#such as color or an optional feature

def make_car(manufacturer,model_name,**car_info):
    "creating a car dictionary"
    car_info['brand'] = manufacturer
    car_info['model'] = model_name
    return car_info

car = make_car('bmw','modelname',color='blue',
               fuel='diesal',condition='used')
print(car)