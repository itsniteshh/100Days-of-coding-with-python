prompt= "\nEnter ur age: "
prompt += "\nEnter 'quit' to exit: "

msg= ""

while msg != "quit":
    msg = input(prompt)

    if msg < "3":
        print("The ticket is free for you")
    elif msg < "12":
        print("The ticket is $10 for you")
    else:
        print(f"As you're {msg}, the ticket is $15 for you")

#need to figure out how loop can be placed here in this program