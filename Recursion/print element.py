def printElements(s,n):
    if n==0:
        return

    printElements(s,n-1)
    print(s[n-1])
x=[1,2,3,4]
printElements(x,4)