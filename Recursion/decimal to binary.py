def convater(n):
    if n==0:
        return ""
    return convater(n//2)+str(n%2)
print(convater(2))