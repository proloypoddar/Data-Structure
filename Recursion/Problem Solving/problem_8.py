def countAbc(x):
    if len(x)<=3:
        return 1
    if x[3:]=="abc"or x[3:]=="aba":
        return 1+countAbc(x[3:])
    else:
        return countAbc(x[1:])
print(countAbc("abaxxaba"))