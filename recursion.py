def recursion(k):
    if k <= 1:
        return 1
    return k*recursion(k-1)
print(recursion(5))