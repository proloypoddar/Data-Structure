def print_all_row(end,n):
    if end>n: 
        return
    one_row(1,end)
    print_all_row(end+1,n)
def one_row(i,end):
    if i==end:
        print(end)
        return
    print(i,end=" ")
    one_row(i+1,end)
print_all_row(1,5)