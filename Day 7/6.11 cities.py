cities= {
    "mumbai" : {
        "country": "India",
        "population": "15 crore",
        "fact": "It is also called, 'City of dreams'"
    },
    "nile": {
        "country": "egypt",
        "population": "3 crores",
        "fact": "It is also called, 'city of the gods'"
    },
    "bihar": {
        "country": "India",
        "population": "10 crore",
        "fact": "It is the birth place of godess Sita"
    }
}

for city, info in cities.items():
    print(f"City name: {city}")
    print(f"It is a city in the country of {info['country']}")
    print(f"It has a total population of {info['population']}")
    print(f"Fact: {info['fact']}\n")