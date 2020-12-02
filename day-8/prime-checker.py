def prime_checker(number):
    for n in range(2,number):
        if number % n == 0:
            print (f"{number} is not a prime number!")
            return 0
    print (f"{number} is a prime number")
    return 0
        

n = int(input("Check this number: "))
prime_checker(number=n)