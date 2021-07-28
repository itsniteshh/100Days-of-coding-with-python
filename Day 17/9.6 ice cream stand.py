""""
class Restaurant:

    def __init__(self, restro_name, cuisine_type):
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        #method 1
        self.number_served = 15

    def describe_restro(self):
        print(f"The restaurant name is {self.restro_name}")
        print(f"It's speciality is {self.cuisine_type} dish")


    def open_restro(Self):
        print(f"{Self.restro_name} is now open for dining")

    def servings(self):
        print(f"The restaurant has served {self.number_served} tables today.")

restro = Restaurant("Hope", "chinese")
#method 2
restro.number_served = 39

restro.describe_restro()
restro.open_restro()
restro.servings()
"""
'''
#method 3
class Restaurant:

    def __init__(self, restro_name, cuisine_type):
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        self.number_served = 15

    def describe_restro(self):
        print(f"The restaurant name is {self.restro_name}")
        print(f"It's speciality is {self.cuisine_type} dish")


    def open_restro(Self):
        print(f"{Self.restro_name} is now open for dining")

    def servings(self):
        print(f"The restaurant has served {self.number_served} tables today.")
    
    def updated_servings(self, new_no):
        self.number_served = new_no

restro = Restaurant("Hope", "chinese")
restro.updated_servings(23)

restro.describe_restro()
restro.open_restro()
restro.servings()
'''

#method 4
class Restaurant:

    def __init__(self, restro_name, cuisine_type):
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        self.number_served = 15

    def describe_restro(self):
        print(f"The restaurant name is {self.restro_name}")
        print(f"It's speciality is {self.cuisine_type} dish")


    def open_restro(Self):
        print(f"{Self.restro_name} is now open for dining")

    def servings(self):
        print(f"The restaurant has served {self.number_served} tables today.")
    
    def updated_servings(self, new_no):
        self.number_served = new_no

    def increment_servings(self, no):
        self.number_served += no

restro = Restaurant("Hope", "chinese")
restro.updated_servings(23)
restro.increment_servings(100)

restro.describe_restro()
restro.open_restro()
restro.servings()


class IceCreamStand:
    def __init__(self, flavors):
        super.__init__()
