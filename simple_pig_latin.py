text = 'Pig latin is cool'
def pig_it(text):
    words = text.split()
    after_editing = []
    for i in words:
        if i.isalpha():  # Check if the word contains only alphabetic characters
            new_string = i[1:] + i[0] + "ay"
            after_editing.append(new_string)
        else:
            after_editing.append(i)  # Keep punctuation marks unchanged
    return " ".join(after_editing)
print(pig_it(text))

#Alternative Solution:

text = 'Pig latin is cool'
def pig_it(text):
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split()])
print(pig_it(text))


    