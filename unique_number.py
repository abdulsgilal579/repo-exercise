def find_uniq(number_list):
    frequency = {}
    for number in number_list:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    for number, count in frequency.items():
        if count == 1:
            return number
        
#Alternative Solution

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b