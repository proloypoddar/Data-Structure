def bunnyEars2(x):
    if x==0:
        return x
    if x%2==0:
        return 3+bunnyEars2(x-1)
    else:
        return 2+bunnyEars2(x-1)
print(bunnyEars2(2))
