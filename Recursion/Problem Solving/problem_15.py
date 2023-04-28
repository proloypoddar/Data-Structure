def endX(x):
    if len(x)==0:
        return ""
    if x[0]=="x":
        return endX(x[1:])+"x"
    else:
        return x[0]+endX(x[1:])
print(endX("xxhixx"))
