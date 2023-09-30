def count11(x):
    if len(x)<2:
        return 0
    if x[:2]=="11":
        return count11(x[2:])+1
    else:
        return count11(x[1:])
print(count11("11bvbcxdcvb11"))