def folding(a, b):
    counter = 0
    while a != 0 and b != 0:
        if a > b:
            counter += a // b
            a = a % b
        else:
            counter += b // a
            b = b % a
    return counter

print(folding(10,7))
