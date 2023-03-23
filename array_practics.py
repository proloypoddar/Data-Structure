a=[10,20,30,40]
def len(x):
    c=0
    for i in x:
        c+=1
    
    return c
def iteration(x):
    for i in range(0,len(x)):
        print(x[i])
def reverseIteration(x):
    for i in range(len(x),-1,-1):
        print(i)
iteration(a)
reverseIteration(a)