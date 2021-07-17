age = "Enter ur age:\n"
age += "Emter 'quit' to exit \n"
active = True

while active:
    msg = input(age)
    if msg == "quit":
        break

    msg = int(msg)
    if msg < 3:
        print("\nThe ticket is free for you")
    elif msg < 12:
        print("The ticket is $10 for you")
    else:
        print(f"As you're {msg}, the ticket is $15 for you\n")

print("Thank you for visiting our theater! You have a nice time ahead")


#complete version of the program..... although i had to look somewhere else