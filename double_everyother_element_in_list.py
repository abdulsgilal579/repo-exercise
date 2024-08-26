# number_list = [1,2,3,4,5,6,7,8]

# def double_every_other(lst):
#     every_second_number = lst[1::2]
#     return every_second_number * 2

# print(double_every_other(number_list))

number_list = [1,2,3,4,5,6,7,8]

for i in range(1, len(number_list), 2):
    number_list[i] *= 2
    print(number_list[i])

print(number_list)