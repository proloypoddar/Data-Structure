def noX(a):
    if len(a)==0:
        return ""
    if a[0]=="x":
        return noX(a[1:])
    else:
        return a[0]+noX(a[1:])
print(noX("xabxb"))