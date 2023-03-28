def bunnyEars2(n):
    if n==0:
        return n
    if n%2==0:
        return 3+bunnyEars2(n-1)
    else:
        return 2+bunnyEars2(n-1)
print(bunnyEars2(2))
    