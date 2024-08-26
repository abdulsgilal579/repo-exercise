Queue = [2,3,10]

def queue_time(customers, n):
    if not customers:
        return 0
    if n==1:
        return sum(customers)
    till_list = [0] * n
    
    for customers_time in customers:
        lest_busy_till = till_list.index(min(till_list))
        till_list[lest_busy_till] += customers_time
    return max(till_list)

print(queue_time(Queue, 2))
