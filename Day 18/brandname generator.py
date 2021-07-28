#1. Create a greeting for your program.
print("hello user!")

#2. Ask the user for the city that they grew up in.
city = input("Enter the city wherein you grew: \n")
#3. Ask the user for the name of a pet.
pet = input("Enter your pet name: \n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city.title() + pet.title()
print(band_name)
