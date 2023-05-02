def hailston(n):
    if n==1:
        print(n,end=" ")
    else:
        if n%2==0:
            print(n,end=" ")
            hailston(n//2)
        else:
            print(n,end=" ")
            hailston(3*n+1)
hailston(13)