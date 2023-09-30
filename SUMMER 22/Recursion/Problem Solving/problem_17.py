def parenBit(x):
    if len(x)==0:
        return ''
    if x[0]=="(":
        if x[-1]==")":
            return x
        else:
            return parenBit(x[:-1])
    return parenBit(x[1:])
print(parenBit("kjda(sd)dfds"))