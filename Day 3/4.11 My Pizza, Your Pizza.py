favFood = ["Chicken Triple Rice", "dum biryani", "paneer chilli"]
print(favFood)


#copying a list
street_food = favFood
print(f" copied list is {street_food}")
street_food.append("burgers")



#inserting to og list
favFood.insert(2, "chinese")
print(favFood)


#proving 2 separate list
print("My fav foods are: ")
for food in favFood:
    print(food)
    
print("\n My fav street foods are: ")
for sfood in street_food:
    print(sfood)