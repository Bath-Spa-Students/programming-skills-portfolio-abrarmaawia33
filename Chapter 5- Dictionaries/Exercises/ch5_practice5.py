# Write a Python program to merge two dictionaries into one.

dict1 = {"a": 0, "b": 2}
dict2 = {"b": 2, "c": 3}

merged_dict = dict1.copy()  
merged_dict.update(dict2)  

print("Merged Dictionary:", merged_dict)
