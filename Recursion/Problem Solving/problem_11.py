def bunnyEars(a):
    if a==0:
        return 0
    return bunnyEars(a-1)+2
print(bunnyEars(2))