sandwich_orders = ['pastrami', "cheese sandwich", "myanose sandwich", 'pastrami', "paneer cheese sandwich", "grilled toast sandwich",  'pastrami', 'pastrami']
finished_sandwich = []

print(f"Sorry to disappoint you but it looks like we have run out of {sandwich_orders[0]}")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
    sandwiches = sandwich_orders
    finished_sandwich.append(sandwiches)



print(f"\nThis is your new order: ")
for orders in sandwich_orders:
    print(orders)
    
print(sandwich_orders)