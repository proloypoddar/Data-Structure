def sum(n):
    if n<=10:
        return n
    x=n%10
    z=sum(n//10)
    return(x+z)
print(sum(12))