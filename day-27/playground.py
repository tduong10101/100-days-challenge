def add(*args):
    result = 0
    for n in args:
        result += float(n)
    return result

print(add(5,5,5,5))