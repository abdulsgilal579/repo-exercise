num = 26899
list_digit = [int(digit) for digit in str(num)]
sorted = list_digit.sort(reverse=True)
combined_list = "".join(sorted)    
