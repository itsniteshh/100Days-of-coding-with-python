current_users = ["admin", "cristiano", "kaka", "lucifier", "itsnitesh"]
new_users = ["lucifier", "morningstar", "captain america", "itsnitesh", "star lord"]

for users in new_users:
    if users == current_users:
        print(f"{users} username already exists")
    else:
        print(f"{users} is available for use")
