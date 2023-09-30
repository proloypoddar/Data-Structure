def strCount(s,c):
    if len(s)<=0:
        return 0
    if s[:len(c)]==c:
        return 1+strCount(s[len(c):],c)
    else:
        return strCount(s[1:],c)
print(strCount("catcowcat", "dog"))