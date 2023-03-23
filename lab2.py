#Name : Polok Poddar
#ID: 21301644

################################
a=input("Enter your String:")
b=input("Enter your 2nd string: ")

if len(a) > 10 or len(b) > 10:
    print("Invalid Input Size")
else:
    x = a + (10 - len(a)) * " "
    y = b + (10 - len(b)) * " "

    lst = [[()]*10, [()]*10]
    for i in range(len(x)):
        if 65 <= ord(x[i]) <= 90:
            upper1 = x[i]
            index1 = i
        lst[0][i] = x[i]
    for j in range(len(y)):
        if 65 <= ord(y[j]) <= 90:
            upper2 = y[j]
            index2 = j
        lst[1][j] = y[j]

    p=f"1st Start:{upper1},{index1}" 
    q=f"2nd Start:{upper2},{index2}"
    print("1st Start: ", upper1, index1)
    print ("2nd Start: ", upper2, index2)
    print(lst)
    flag = True
    while flag:
        user_input = input("Enter any character other than q to display billboard or q to exit: ")
        if user_input == 'q':
            flag = False
            print(p)
            print(q)
        else:
            index1 = (index1 - 1 + 10) % 10
            index2 = (index2 + 1) % 10
            upper1 = lst[0][index1]
            upper2 = lst[1][index2]
            # print("Start: ", upper1, index1)
            # print("Start: ", upper2, index2)
            for i in range(10):
                print(lst[0][(index1 + i) % 10], end="")
            print("\n")
            for j in range(10):
                print(lst[1][(index2 + j) % 10], end="")
            print("\n")
