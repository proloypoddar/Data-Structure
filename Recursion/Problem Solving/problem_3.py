def count7(x):
    if x==0:
        return x
    if x%10==7:
        return 1+count7(x//10)
    else:
        return count7(x//10)
print(count7(7777777))
