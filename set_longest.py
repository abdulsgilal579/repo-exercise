#My_solution

def longest(a1, a2):
    items =set()
    for i in a1:
        items.add(i)
    for i in a2:
        items.add(i)
    sorted_items = sorted(items)
    join_items = "".join(sorted_items)
    return join_items

#alternative_soultion

def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))
