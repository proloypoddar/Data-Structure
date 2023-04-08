def print_array(x):
    if len(x)==0:
        return
    print(x[0])
    print_array(x[1:])
print_array("acjhcj")