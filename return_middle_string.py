def get_middle(s):
    length_of_string = int(len(s))
    if length_of_string % 2 == 0:
        first_middle = (length_of_string//2) -1
        second_middle = (length_of_string//2)
        return f"{s[first_middle]}{s[second_middle]}"
    else:
        middle_value = (length_of_string//2)
        return s[middle_value]



