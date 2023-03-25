def print_pattern(n, i=1):
    if i <= n:
        print_row(n, i)
        print_pattern(n, i+1)

def print_row(n, i, j=1):
    if j <= n:
        if j < n-(i-1):
            print('  ', end='')
        else:
            print(j-(n-i), end=' ')
        print_row(n, i, j+1)
    else:
        print('')

print_pattern(5)
