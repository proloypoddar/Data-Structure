def remove(array,num):
    x=0
    while x<len(array):
        if array[x]==num:
            c=x
            x+=1
            for i in range(c,len(array)):
                array[x]=array[x+1]
    return array
array=[10,20,30,40,50,60]
print(remove(array,40))