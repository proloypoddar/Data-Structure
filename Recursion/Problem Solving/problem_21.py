def allStar(a):
    if len(a)<=1:
        return a
    if len(a)!=0:
        return a[0]+"*"+allStar(a[1:])
    return allStar(a[1:])+"*"
print(allStar("hello"))