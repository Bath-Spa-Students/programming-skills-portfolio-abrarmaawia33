# Program that uses a function to check if a given number is prime or not
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

