def triangle(a):
    if a==0:
        return 0
    if a==1:
        return 1
    return triangle(a-1)+2
print(triangle(3))