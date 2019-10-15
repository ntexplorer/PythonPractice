def carInfo(manufacture, model, **user_info):
    carInfo = {}
    carInfo["manufacture"] = manufacture
    carInfo["model"] = model
    for key, value in user_info.items():
        carInfo[key] = value
    return carInfo

car = carInfo('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
