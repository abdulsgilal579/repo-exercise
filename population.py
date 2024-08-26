import math

def nb_year(p0, percent, aug, p):
    counter_year = 0
    estimated_population = p0
    percent = percent / 100  # Convert percentage to a decimal
    while estimated_population < p:
        estimated_population += math.floor(estimated_population * percent + aug)
        counter_year += 1
    return counter_year

