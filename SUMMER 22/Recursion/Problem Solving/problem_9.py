def countHi2(x):
    if len(x)<=2 or x[0]=="x":
        return 0
    if x[0]=="x":
        return
    else:
        if x[:2]=="hi":
            return 1+countHi2(x[2:])
        else:
            return countHi2(x[1:])
print(countHi2("ahixhi"))