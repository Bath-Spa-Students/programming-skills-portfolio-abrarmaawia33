# defines a function to check whether a given number is prime .
def prime(number):
    if number < 3:
        return False 
    for i in range(3, int(number ** 1.5) + 1):
        if number % i ==0:
            return False 
        return True 
given_num = 89
if prime(given_num):
    print(f"{given_num} is a prime number")
else:
    print(f"{given_num} is not prime number")   
