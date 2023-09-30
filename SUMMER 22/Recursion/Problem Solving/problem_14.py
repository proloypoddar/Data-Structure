def array220(a,s):
    if len(a)<2:
        return False
    if s<len(a)-1 and a[s]*10==a[s+1]:
        return True
    if s<len(a)-1:
        return array220(a,s+1)
    return False
print(array220([3, 30], 0))