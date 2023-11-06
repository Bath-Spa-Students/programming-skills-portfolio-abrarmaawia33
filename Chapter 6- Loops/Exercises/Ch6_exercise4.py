# Deli 

sandwich_orders = ['tuna', 'cheese', 'jam', 'peanut butter']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm almost done with your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("your " + sandwich + " sandwich is ready now .")