def is_isogram(string):
    lowercase_string = string.lower()
    seen_characters = ()
    for char in lowercase_string:
        if char.isspace():
            continue
        if char in seen_characters():
            return False
        seen_characters.add(char)
    return True
        


