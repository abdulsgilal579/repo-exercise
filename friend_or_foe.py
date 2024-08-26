list_of_friends =  ["Ryan", "Kieran", "Jason", "Yous"]

def friend_list_filtered(list):
    friend_list_filtered = []
    for i in list:
        if len(i) == 4:
            friend_list_filtered.append(i)
    return friend_list_filtered

print(friend_list_filtered(list_of_friends))