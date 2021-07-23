'''
def car_info(manufacturer, model_name, **about_car):
    about_car ["manufacturer"] = manufacturer
    about_car ["model name"] = model_name
    return about_car

cars = car_info("Ford", "Mustang", color = "Yellow", S_feature = "Used as Bumblebee")
print(cars)

print("\nThe following are the details about the car I'm planning to buy")
for car, info in cars.items():
    print(info)
    '''

