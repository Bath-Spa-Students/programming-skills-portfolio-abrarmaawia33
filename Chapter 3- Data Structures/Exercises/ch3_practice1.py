# list 
# Given a Python list, write a program to remove all occurrences of item 20.

list = [5, 20, 15, 20, 25, 50, 20]
item_remove = 20

while item_remove in list:
    list.remove(item_remove)

print(list)
 
  