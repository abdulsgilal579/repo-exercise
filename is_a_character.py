import string
def is_it_letter(s):
    letter_list = [letter for letter in string.ascii_letters]
    if s.lower() in letter_list:
        return True
    else:
        return False

print(is_it_letter("s"))



