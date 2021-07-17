toppings = "Enter which toping you'd like: "
msg = ""


while msg != "quit":
    msg = input(toppings)
    if msg == "quit":
        break

    else:
        print(f"We'll add {msg} to your pizza\n")

print(f" \nWe'll call you once your order is ready.")

