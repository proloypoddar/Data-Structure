# def right_shift(array):
#     temp=array[len(array)-1]
#     x=len(array)-1
#     while x>0:
#         array[x]=array[x-1]
#         x-=1
#     array[0]=temp
#     return array
# import numpy as np
# array=np.array([10,20,30,40,50,60])
# beats=np.array([1,0,0,1,0,1])
# def playRight(array,beats):
#     for i in beats:
#         if i==1:
#             right_shift(array)
#     return array
# print(playRight(array,beats))
#############################
# task2:
# import numpy as np

# cards = np.array([10, 2, 30, 2, 50, 2, 2, 0, 0])

# def discardCards(cards, number):
#     pos = 0
#     for i in range(len(cards)):
#         if cards[i] != number:
#             cards[pos] = cards[i]
#             pos += 1
#     for i in range(pos, len(cards)):
#         cards[i] = 0
#     return cards
# print(discardCards(cards, 2))

#####################
# task 3:
# import numpy as np

# pokemon_1 = np.array([4, 5, -1, None, None])
# pokemon_2 = np.array([2, 27, 7, 12, None])

# def mergeLineup(pokemon_1, pokemon_2):
#     for i in range(len(pokemon_1)):
#         if pokemon_1[i] is None:
#             pokemon_1[i] = 0
#         if pokemon_2[len(pokemon_2) - 1 - i] is None:
#             pokemon_2[len(pokemon_2) - 1 - i] = 0
#         pokemon_1[i] = int(pokemon_1[i] + pokemon_2[len(pokemon_2) - 1 - i])
#     return pokemon_1
# result = mergeLineup(pokemon_1, pokemon_2)
# print(result)

#######################################
# task4
# def balanceSalami(salami):
#     if len(salami)<0:
#         return 0
#     total=0
#     for i in range(len(salami)):
#         total+=salami[i]
#     a = 0
#     b = 0
#     for i in range(len(salami)):
#         a += salami[i]
#         b = total - a
#         if a == b:
#             return True
#     return False
# salami = [2, 1, 1, 2, 1]
# result = balanceSalami(salami)
# print(result)
###########################################3
#task 5
# def protectSalami(salami):
#     a = None
#     c_1 = 0
#     b = None
#     c_2 = 0
#     for i in salami:
#         if i == a:
#             c_1 += 1
#         elif i == b:
#             c_2 += 1
#         elif c_1 == 0:
#             a = i
#             c_1 = 1
#         elif c_2 == 0:
#             b = i
#             c_2 = 1
#         else:
#             c_1 -= 1
#             c_2 -= 1
#     c_1 = 0
#     c_2 = 0
#     for i in salami:
#         if i == a:
#             c_1 += 1
#         if i == b:
#             c_2 += 1

#     if c_1 >= 2 and c_2 >= 2 and c_1 ==c_2:
#         return True
#     else:
#         return False
# salami = [3,4,6,3,4,7,4,6,8,6,6]
# result1 = protectSalami(salami)
# print(result1)
###########################
# task 6
import numpy as np
arr=np.array([2,12,3,8,1,5])
def waveYourFlag(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] % 2 == 0:
            if arr[i + 1] % 2 != 0:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i + 1] % 2 == 0:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
result = waveYourFlag(arr)
print(result)
