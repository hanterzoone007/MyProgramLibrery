import string

a_string = list(string.ascii_letters)
b_string = list(string.ascii_letters)

def shift(n):
    for i in range(n):
        letter = b_string[0]
        b_string.pop(0)
        b_string.append(letter)

text = 'Hello, world!'
shift(10)
new_text = []
for i in text:
    if i in a_string:
        b_index = a_string.index(i)
        new_text.append(b_string[b_index])
    else:
        new_text.append(i)
    
print(''.join(new_text))
