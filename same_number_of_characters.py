word = "xxommm"

def xo(s):
    x_counter = 0
    o_counter = 0
    for i in s:
        lc_character = i.lower()
        if lc_character == "x":
            x_counter += 1
        elif lc_character == "o":
            o_counter += 1
        else:
            pass
    if x_counter == o_counter:
        return True
    else:
        return False

print(xo(word))


    
    