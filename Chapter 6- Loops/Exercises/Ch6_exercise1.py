# Pizza Toppings (loops)

prompt = "\nWhat topping would you like put on your pizza?"
prompt += "\nEnter 'quit' when you are  done: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break