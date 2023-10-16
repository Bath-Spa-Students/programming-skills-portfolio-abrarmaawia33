guests = ['aryam', 'shahad', 'masara']

name = guests[0].title()
print(name + ", I would like to invite you for a dinner.")

name = guests[1].title()
print(name + ",I would like to invite you for a dinner .")

name = guests[2].title()
print(name + ", I would like to invite you for a dinner.")

name = guests[0].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[0])
guests.insert(0, 'mayada')

name= guests[0].title()
print(name + ",I would like to invite you for dinner .")

name = guests[1].title()
print(name + ",I would like to invite you for a dinner .")

name = guests[2].title()
print(name + ", I would like to invite you for a dinner.")