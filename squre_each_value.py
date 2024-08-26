numbers_list = [1,2,3,4,5,6,7,8,9,0]
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i**2
    return sum

print(square_sum(numbers_list))