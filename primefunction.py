def is_prime(num):
    if num<=1:
        return false

    for i in range(2,num):
if num%i==0: 
        return false

    return True

#Taking input from user

n=int(input("Enter a number:"))

if is_prime(n)
    print(n,"is a prime number")

else:
    print(n,"is not a prime number")
