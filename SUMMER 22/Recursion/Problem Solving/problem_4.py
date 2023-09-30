def countX(x):
    if len(x)==0:
        return 0
    if x[0]=="x":
        return 1+countX(x[1:])
    else:
        return countX(x[1:])
print(countX("xxxx"))