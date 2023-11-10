# Write a Python program to iterate through both the keys and values of a dictionary and print them .

my_dict = {
    "name": "Abrar Maawia",
    "age": 18,
    "location": "UAE",
    "hobbies": ["Painting", "reading", "playing piano"],
}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")