data = {
    "usha": 0,
    "veena": 0,
    "kavita": 0,
    "rohit": 0,
    "sujit": 0,
    "mayur": 0,
    "total_candies": 25,
    "total_value": 225
}


def outed(meet):
    sum_of_values = 0
    total_number_of_people = 0
    for i in meet:
        total_number_of_people += 1
    print(total_number_of_people) 
    for value in meet.values():
        sum_of_values += value
    happiness_value = sum_of_values/total_number_of_people
    #print(happiness_value)
    return happiness_value

print(outed(data))