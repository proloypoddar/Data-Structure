def right_shift(array):
    x=len(array)-1
    while (x>0):
        array[x]=array[x-1]
        x-=1
    array[0]=0
    return array
array=[10,20,30,40,50]
print(right_shift(array))
print(right_shift(array))
print(right_shift(array))
