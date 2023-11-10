# Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target_number = 8

for number in numbers:
    print(number)
    
    if number == target_number:
        print(f"Found the target number {target_number}. Exiting the loop.")
        break

