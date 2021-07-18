responses = {}
poll = True


while poll:
    name = input("\nEnter ur name: ")
    location = input("Enter a location you'd like to visit next year: ")

    responses [name] = location

    repeat = input("Do you want to repeat the poll? (yes/no) \n")
    if repeat == "no":
        poll = False
    elif repeat == "yes":
        poll = True
    else: 
        print("wrong input! Repeat the steps again")
        for answer in repeat:
            repeat = input("Do you want to repeat the poll? (yes/no) \n")

    
for key, value in responses.items():
    print(f"{key} would like to visit {value} someday.\n")
print(responses)