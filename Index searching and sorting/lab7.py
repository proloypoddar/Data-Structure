class KeyIndex:
    def __init__(self, a):
        self.a = a
        self.max = a[0]
        self.min = a[0]
        for i in a:
            if i > self.max:
                self.max = i
            if i < self.min:
                self.min = i
        self.aux = [0] * (self.max - self.min + 1)
        for i in a:
            self.aux[i - self.min] += 1
        print(self.aux)
    def search(self, k):
        if k < self.min or k > self.max:
            return False
        else:
            return True
    def sort(self):
        new_array = [0] * len(self.a)
        z = [0] * (self.max - self.min + 1)
        for i in self.a:
            z[i - self.min] += 1
        for i in range(1, len(z)):
            z[i] += z[i-1]
        for i in range(len(self.a)-1, -1, -1):
            new_array[z[self.a[i] - self.min] - 1] = self.a[i]
            z[self.a[i] - self.min] -= 1
        return new_array
a = KeyIndex([1, 2, 4, -5, -6, 6, 5, 6, 5])
print(a.search(9))
print(a.sort())
class TestKeyIndex:
    def test_search(self):
        # Test with various search inputs
        a = KeyIndex([1, 2, 4, -5, -6, 6, 5, 6, 5])
        if a.search(2) != True:
            print("Search test failed for input 2")
        if a.search(-6) != True:
            print("Search test failed for input -6")
        if a.search(0) != False:
            print("Search test failed for input 0")
        if a.search(9) != False:
            print("Search test failed for input 9")
        else:
            print("Search tests passed.")

    def test_sort(self):
        # Test if the sorted output is correct
        a = KeyIndex([1, 2, 4, -5, -6, 6, 5, 6, 5])
        sorted_array = a.sort()
        for i in range(len(sorted_array) - 1):
            if sorted_array[i] > sorted_array[i + 1]:
                print("Sort test failed")
                return
        print("Sort test passed.")

test = TestKeyIndex()
test.test_search()
test.test_sort()


# ######################
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
