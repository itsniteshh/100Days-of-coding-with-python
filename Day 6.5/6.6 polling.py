favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

person = ["nitesh", "arjun", "nishit", "jen", "phil"]

for names in favorite_languages.keys():
    if names in person:
        print(f'{names} has already taken the poll')
    else:
        print(f"{names} needs to take the poll")