def groupSum5(start,array,target):
    if target==0:
        return True
    if start >= len(array):
        return False
    if array[start]%5==0:
        if start <len(array)-1 and array[start+1]==1:
            return groupSum5(start+2,array,target-array[start])
        else:
            return groupSum5(start+1,array,target-array[start])
    return groupSum5(start+1,array,target) or groupSum5(start + 1, array, target - array[start])
print(groupSum5(0, [2, 5, 10, 4], 19))
