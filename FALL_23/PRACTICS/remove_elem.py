def remove(source, idx):
    for idx in range(idx, len(source)):
        if idx != len(source) - 1:
            source[idx] = source[idx + 1]
        elif idx == len(source) - 1:
            source[idx] = 0
    return source
a=[10,20,30,40,50,60]
print(remove(a,3))