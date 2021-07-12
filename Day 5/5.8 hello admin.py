username = ["admin", "cristiano", "kaka", "lucifier", "itsnitesh"]
name = input("Enter ur username: ")

if name in username:
    if "admin" in name:
        print("Hello admin! would you like to check the status report of the website")
    
    else:
        print(f"Hello {name}, thank you for joining in again")

else:
    print("username doesn't exists! create new account")

#this is the high version programs