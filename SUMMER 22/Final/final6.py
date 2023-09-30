def insert(arr,elem):
    if len(arr)==0:
        return arr
    if len(arr)<len(elem):
        new_arr=0*len(arr)
        new_arr=new_arr+arr
        for i in range(len(new_arr)):
            new_arr[len(arr)+1]=elem[i]
        return new_arr
print(insert([1,2,3,4,5],[6,7,8]))
