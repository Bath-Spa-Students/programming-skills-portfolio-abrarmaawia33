# No Pastrami 

sandwich_orders = ['tuna', 'cheese', 'jam', 'pastrami', 'peanut butter', 'chicken', 'honey', 'pastrami', 'pastrami']

print("Sorry, we've run out of pastrami sandwiches.")


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


finished_sandwiches = []


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Almost done with your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
