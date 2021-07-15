fav_actors = {
    "Shahrukh Khan": {
        "movies": ["Swades", "My name is Khan", "DDLJ", "Don"],
        "lives": "Mumbai",
        "nickname": "king of bollywood"
    },
    "sushant singh rajput": {
        "movies": ["Chichhore", "Dhoni", "Raabta"],
        "lived" : "Mumbai",
        "nickname": "Man who won everyone's heart"
    },
    "Tom Cruise": {
        "movies": ["Mission Impossible", "John Maguire", "Edge of tomorrow"],
        "lives": "Neywork",
        "nickname": "world's richest hero"
    }
}

for actors, info in fav_actors.items():
    if "sushant singh rajput" in actors:
        print(f"My favourite actor is: Late {actors.title()}")
        print(f"Some of his movies were: \n\t{info['movies']}")
        print(f"People used to call him {info['nickname']}\n")
    
    else:
        print(f"My favourite actor is: {actors}")
        print(f"Some of his movies are: \n\t{info['movies']}")
        print(f"People also call him {info['nickname']}\n")