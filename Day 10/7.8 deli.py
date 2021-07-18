sandwich_orders = ['pastrami', "cheese sandwich", "myanose sandwich", 'pastrami', "paneer cheese sandwich", "grilled toast sandwich",  'pastrami', 'pastrami']
finished_sandwich = []

while sandwich_orders:
    orders = sandwich_orders.pop()

    print(f"Your {orders} is being cooked!")

    finished_sandwich.append(orders)

print("\nFollowing orders have been made: ")

for sandwiches in finished_sandwich:
    print(sandwiches)