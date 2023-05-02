def FibonacciSearch(lys, val):
    fibM2 = 0
    fibM1 = 1
    fibM = fibM1 + fibM2
    while (fibM < len(lys)):
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM1 + fibM2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            index = i
        elif (lys[i] > val):
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        else :
            return i
    if(fibM1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1

print(FibonacciSearch([1,2,3,4,5,6,7,8,9,10,11], 2))