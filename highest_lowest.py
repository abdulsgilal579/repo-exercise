def high_and_low(numbers):
    numbers_list = numbers.split()
    highest_number = int(numbers_list[0])

    for i in numbers_list:
        num = int(i)
        if num > highest_number:
            highest_number = num

    lowest_number = int(numbers_list[0])
    for i in numbers_list:
        num = int(i)
        if num < lowest_number:
            lowest_number = num
            
    return f"{highest_number} {lowest_number}"
    
print(high_and_low("2 3 4 5 6 7 8 9"))