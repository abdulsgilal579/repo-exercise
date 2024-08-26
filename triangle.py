#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29

def row_sum_odd_numbers(n):
    current_odd = 1
    for i in range(1, n+1):
        print(" "*(n-i)*2, end="")
        for j in range(i):
            print(f"{current_odd:>4}", end="")
            current_odd += 2
        print()
    return n**3
    

print(row_sum_odd_numbers(296))


    