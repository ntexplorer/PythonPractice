def city_country(city, country):
    fullName = city + ", " + country
    return fullName.title()


place = city_country(input("Please enter city name: "), input("Please enter country name: "))
print(place)
