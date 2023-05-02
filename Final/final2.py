def reverse(s):
    if len(s)==0:
        return s
    return reverse(s[1:])+[s[0]]
print(reverse([1,2,3,4,5]))