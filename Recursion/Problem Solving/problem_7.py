def pairStar(x):
    if len(x)<2:
        return x
    if x[0]==x[1]:
        return x[0]+"*"+x[1]+pairStar(x[2:])
    else:
        return x[0]+pairStar(x[1:])
print(pairStar("jfhlld"))