def strCopies(s, sub, num):
    if num == 0:
        return True
    if len(s) < len(sub):
        return False
    if s[:len(sub)] == sub:
        return strCopies(s[1:], sub, num-1)
    else:
        return strCopies(s[1:], sub, num)


print(strCopies("catcowcat", "cow", 2))

