# class KeyIndex:
#     def __init__(self,a):
#         self.a=a
#         x=a[0]
#         for i in self.a:
#             if i>x:
#                 x=i
#         self.aux=[0]*int(x+1)
#         for i in self.a:
#             if i<0:
#                 a=i*(-1)
#                 self.aux[a]+=1
#             else:
#                 self.aux[i]+=1
#         print(self.aux)
#     def search(self, k):
#         if k < 0 or k >= len(self.aux):
#             return 0
#         else:
#             return self.aux[k]
#     def sort(self):
#         a = [0] * len(self.a)
#         index = 0
#         for i in range(len(self.aux)):
#             count = self.aux[i]
#             for j in range(count):
#                 a[index] = i
#                 index += 1
#         return a
# a=KeyIndex([1,2,4,-5,-6,6,5,6,5])
# print(a.search(2))
# print(a.sort())
# ######################
# Hash function calculation, method properly written:
def is_digit(char):
    digits = ["0123456789"]
    if char in digits:
        return True
    else:
        return False
def hash_function(string):
    consonants = ["BCDFGHJKLMNPQRSTVWXYZ"]
    num_consonants = 0
    for char in string:
        if char in consonants:
            num_consonants += 1
    digit_sum = 0
    for char in string:
        if char.isdigit():
            digit_sum += int(char)
    hash_val = (num_consonants * 24 + digit_sum) % 9
    return hash_val
print(hash_function('ST1E89B8A32'))
#########################################################