
def hotel_cost(nights):
    return 140* nights

#define a function called plane_ride_cost thet takes a string, city as input.
def plane_ride_cost (city):
    if "Charlotte"== city:
        return 183
    elif "Tampa"== city:
        return 220 
    elif "Pittsburgh"== city:
        return 222 
    elif "Los Angels"== city:
        return 475 
    
#define a functiom called rental_car_cost with an arguement called days
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else :
        return 40*days

#define a function called trip cost with arguement day,money and city
def trip_cost 