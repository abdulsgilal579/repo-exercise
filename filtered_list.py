def filter_list(l):
    new_list = []
    for i in l:
        if isinstance(i, int) and i >= 0:
            new_list.append(i)
    return new_list



