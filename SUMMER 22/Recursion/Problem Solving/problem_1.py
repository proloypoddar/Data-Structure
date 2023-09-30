def sumDigits(x):
    if x<=10:
        return x
    n=x%10
    z=sumDigits(x//10)
    return(n+z)
print(sumDigits(6))
