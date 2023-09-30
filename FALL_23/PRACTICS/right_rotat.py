def right_rotat(array):
    temp=array[len(array)-1]
    x=len(array)-1
    while x>0:
        array[x]=array[x-1]
        x-=1
    array[0]=temp
    return array
array=[10,20,30,40,50]
print(right_rotat(array))
print(right_rotat(array))
print(right_rotat(array))
