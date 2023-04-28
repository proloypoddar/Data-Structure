def array6(a,num):
    if len(a)==0:
        return False
    if a[0]==6:
        return True
    else:
        return array6(a[1:],num+1)
print(array6([1,4],0))
