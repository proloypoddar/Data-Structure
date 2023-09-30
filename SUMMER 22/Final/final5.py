def add(arr1, arr2):
    x = len(arr1)
    y = len(arr2)
    y2 = [arr2[y-1-i] for i in range(y) if arr2[y-1-i] is not None]
    if x > y:
        a = [0] * x
        for i in range(len(a)-1):
            if i < len(y2):
                a[i] = int(y2[i]) + int(arr1[i])
            else:
                a[i] = int(arr1[i])
        return a
    else:
        a = [0] * y
        for i in range(len(a)-1):
            if i < len(y2):
                a[i] = int(y2[i]) + int(arr1[i])
            else:
                a[i] = int(arr1[i])
        return a

arl = [1, 4, 5, 8, None, None, None]
ar2 = [7, 4, 8, 9, 5, None, None]

ar3 = add(arl, ar2)

print(ar3)
