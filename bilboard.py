import time
def billboard(text1, text2):

    billboard = [[" " for j in range(10)] for i in range(2)]
    index1 = 0
    index2 = 9
    for i in range(20):
        for j in range(2):
            for k in range(10):
                billboard[j][k] = " "
        for j in range(min(len(text1), 10)):
            billboard[0][(j + index1) % 10] = text1[j]

        for j in range(min(len(text2), 10)):
            billboard[1][(j + index2) % 10] = text2[j]
        for j in range(2):
            print("".join(billboard[j]))
        index1 = (index1 - 1 + 10) % 10
        index2 = (index2 + 1) % 10
        time.sleep(1)
text1 = "JOY BANGLA"
text2 = "PROLOY $"
billboard(text1, text2)
