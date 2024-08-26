#Solution_01

dic_data = {"Java": 10, "Ruby": 65, "Python": 80}
def value(key):
    return dic_data[key]
sorted_keys = sorted(dic_data, reverse=True, key=value)
print(sorted_keys)

#Solution_02

def my_languages(results):
    passing_languages = {key: value for key, value in results.items() if value >= 60}
    sorted_languages = sorted(passing_languages, reverse=True, key=lambda key: passing_languages[key])
    return sorted_languages