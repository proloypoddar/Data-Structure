def changePi(x):
    if len(x)==0:
        return ""
    if x[:2]=="pi":
        return "3.14"+changePi(x[2:])
    else:
        return x[0]+changePi(x[1:])

print(changePi("xpix"))