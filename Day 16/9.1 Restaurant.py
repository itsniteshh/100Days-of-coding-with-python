class Restaurant:

    def __init__(self, restro_name, cuisine_type):
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type

    def describe_restro(self):
        print(f"The restaurant name is {self.restro_name}")
        print(f"It's speciality is {self.cuisine_type} dishes")


    def open_restro(Self):
        print(f"{Self.restro_name} is now open for dining")

restro = Restaurant("Hope", "chinese")

restro.describe_restro()
restro.open_restro()