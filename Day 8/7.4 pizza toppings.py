toppings = "Enter which toping you'd like: "
msg = ""

while msg != "quit":
    msg = input(toppings)
    if msg != "quit":
        print(f"\nWe'll add {msg} to your pizza")

    elif msg == "quit":
        break

print(f" \nWe'll call you once your order is ready.")
#need to make this to list format
