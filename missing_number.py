def missing_no(nums):
    number_list = [x for x in range(0, 101)]
    missing_numbers = None

    for i in number_list:
        if i not in nums:
            missing_numbers = i

    return missing_numbers
