for n in range(1,101):
    if n % 15 == 0:
        n = 'fizzbuzz'
    elif n % 3 == 0:
        n = 'fizz'
    elif n % 5 == 0:
        n = 'buzz'
    print(n)