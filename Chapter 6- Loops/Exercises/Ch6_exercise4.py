# Deli ( sandwish list)

sandwich_orders = ['tuna', 'cheese', 'jam', 'peanut butter', 'chicken', 'honey']

finished_sandwiches = []

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
