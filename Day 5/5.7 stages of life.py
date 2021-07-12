age = int(input("Enter ur age: "))

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("you are a kid")
elif age < 20:
    print("You are a teen")
elif age <65:
    print("you're an adult")
else:
    print("you're an elder")