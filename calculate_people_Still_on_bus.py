def number(bus_stops):
    sum_off = 0
    sum_on = 0
    for i in bus_stops:
        people_get_on_bus = i[0]
        people_get_off_bus = i[1]
        sum_off += people_get_off_bus
        sum_on += people_get_on_bus
    return sum_on - sum_off