import string


def encrypt(lines):
    shag = 1
    letters = string.ascii_letters
    res = []
    for line in lines:
        encrypted_text = ""
        for char in line:
            place = letters.find(char)
            new_place = place + shag
            if char in letters:
                encrypted_text += letters[new_place]
            else:
                encrypted_text += char
        shag += 1
        res.append(encrypted_text)
    return res


with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = encrypt(lines)

with open('output.txt', 'w') as file:
    file.write(''.join(result))

