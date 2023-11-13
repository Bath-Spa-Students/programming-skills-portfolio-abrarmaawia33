# 
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


#khgyg

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers_to_check = [17, 21, 29, 50, 97]

for number in numbers_to_check:
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
