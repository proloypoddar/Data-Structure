import numpy as np
def two_sums(nums, target):
    dict = {}
    for i in range(len(nums)):
        num = nums[i]
        x = target - num
        if x in dict:
            return [dict[x], i]
        dict[num] = i
nums = np.array([2, 1, 0, 0, 2, 2, 4, 3])   
target = 43 % 10  
result = two_sums(nums, target)
print(result)