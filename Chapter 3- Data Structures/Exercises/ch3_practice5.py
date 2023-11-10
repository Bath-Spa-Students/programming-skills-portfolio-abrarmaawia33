#  Write a program to find value 20 in the list, and if it is present, replace it with 200.

list = [5, 10, 15, 20, 25, 50, 20]
value_to_find = 20
replacement_value = 200
found = False 

for i in range(len(list)):
    if list[i] == value_to_find:
        list[i] = replacement_value
        found = True
        break  

if found:
    print("Value 20 replaced with 200 in the list:", list)
else:
    print("Value 20 not found in the list.")

