def square_digits(num):
    number_list = [int(digit) for digit in str(num)]
    new_list = []
    for i in number_list:
        new_list.append(str(i**2))
    connected_list = int("".join(new_list))
    print(type(connected_list))
    return connected_list

print(square_digits(9999))
