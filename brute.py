def maxArray(arr):
    n = len(arr)
    max_sum =-9999999999999999999999999999999999999999
    maxSubarray = []
    for i in range(n):
        for j in range(i,n):
            subArray = arr[i:j+1]
            subArraySum = sum(subArray)
            if subArraySum > max_sum:
                max_sum = subArraySum
                maxSubarray = subArray
    print(maxSubarray)
    print(max_sum)
arr = [-5,4,6,-3,4,-1]
maxArray(arr) 