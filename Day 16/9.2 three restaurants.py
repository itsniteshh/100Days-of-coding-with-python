class Restaurant:

    def __init__(self, restro_name, cuisine_type):
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type

    def describe_restro(self):
        print(f"The restaurant name is {self.restro_name}")
        print(f"It's speciality is {self.cuisine_type} dishes")


    def open_restro(Self):
        print(f"{Self.restro_name} is now open for dining\n")

restro_1 = Restaurant("Hope", "chinese")
restro_1.describe_restro()
restro_1.open_restro()

restro_2 = Restaurant("pegasus", "Thai")
restro_2.describe_restro()
restro_2.open_restro()

restro_3 = Restaurant("Optimus", "Italian")
restro_3.describe_restro()
restro_3.open_restro()
