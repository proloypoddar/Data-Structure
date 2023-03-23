def mean(x):
    a=0
    for i in range(len(x)):
        a=a+x[i]
        m=a/len(x)
    return(m)

def st_dev(x):
    a=0
    for i in range(len(x)):
        a=a+x[i]
        m=a/len(x)
    s=0
    for i in range(len(x)):
        s=s+(x[i]-m)**2
    v=s/len(x)
    st=v**0.5
    return(st)

def new(x):
    a=0
    b=0
    for i in range(len(x)):
      
        if x[i]>=a:
            a=x[i]
        if x[i]<=b:
            b=x[i]
    print(a,b)


def sd_array(x):
    a=0
    for i in range(len(x)):
        a=a+x[i]
        m=a/len(x)
    s=0
    for i in range(len(x)):
        s=s+(x[i]-m)**2
    v=s/len(x)
    st=v**0.5
    c=0
    for j in range(len(x)):
        if (x[j]-m)>=1.5*st or (x[j]-m)<=-1.5*st:
            c+=1
    lst=[0]*c
            
    i=0
    for j in range(len(x)):
        if (x[j]-m)>=1.5*st or (x[j]-m)<=-1.5*st:

            lst[i]=x[j]
            i+=1
    print(lst)

sou=[10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
print(st_dev(sou))
print(mean(sou))
new(sou)
sd_array(sou)