#Hash function calculation, method properly written:
def is_digit(char):
    digits = "0123456789"
    if char in digits:
        return True
    else:
        return False
def hash_function(string):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    num_consonants = 0
    for char in string:
        if char in consonants:
            num_consonants += 1
    digit = 0
    for char in string:
        if is_digit(char):
            digit += int(char)
    value = (num_consonants * 24 + digit) % 9
    return value
print(hash_function("ST1E89B8A32"))

# Linear probing properly implemented:
def is_digit(char):
    digits = "0123456789"
    if char in digits:
        return True
    else:
        return False
def hash_function(string, hash_table):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    num_consonants = 0
    for char in string:
        if char in consonants:
            num_consonants += 1
    digit = 0
    for char in string:
        if is_digit(char):
            digit += int(char)
    value = (num_consonants * 24 + digit) % 9
    if hash_table[value] is None:
        hash_table[value] = string
    else:
        index = (value + 1) % len(hash_table)
        while hash_table[index] is not None:
            index = (index + 1) % len(hash_table)
        hash_table[index] = string
    return hash_table


hash_table = [None] * 9

strings = ['ST1E89B8A32',"ST1E89B8A32",'ABCD1234',"ST1E89B8A32","ST1E89B8A32",'XYZ4567']
for string in strings:
    hash_function(string, hash_table)
print(hash_table)
