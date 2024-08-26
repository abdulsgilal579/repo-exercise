#my_solution

import math
number_list = [55,95,62,36,48]

def distances_from_average(test_list):
    overall_average = sum(test_list)/len(test_list)
    difference_avg = []
    for i in test_list:
        difference = round((overall_average - i),2)
        difference_avg.append(difference)
    return difference_avg
print(distances_from_average(number_list))

#alternative_solution

number_list = [55, 95, 62, 36, 48]
def distances_from_average(test_list):
    overall_average = sum(test_list) / len(test_list)
    return [round(overall_average - x, 2) for x in test_list]
print(distances_from_average(number_list))

