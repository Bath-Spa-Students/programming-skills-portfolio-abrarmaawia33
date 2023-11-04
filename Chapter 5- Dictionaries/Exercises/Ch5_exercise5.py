# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'bird',
    'name': 'meme',
    'owner': 'abrar',
    'weight': 10,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'kity',
    'owner': 'phoebe',
    'weight': 25,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'buddy',
    'owner': 'kairi',
    'weight': 40,
    'eats': 'meet',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))