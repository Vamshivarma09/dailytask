# import math

# def jumSearch(arr, target,n):
#     arr.sort()
#     print(arr)
#     step = int(math.sqrt(n))
#     prev = 0
#     while arr[int(min(step,n))-1] < target:
#         prev = step
#         step += (int(math.sqrt(n)))
#         if prev>=n:
#             return None
        
#     while arr[int(prev)]<target:
#         prev = prev+1
#         if prev == min(step,n):
#             return None
#     if arr[int(prev)] == target:
#         return prev
#     else:
#         return None
# arr = [99,88,100,103,105,107,876]
# target = 876
# n = len(arr)
# print("the position of target is ", jumSearch(arr,target,n))

import math

def jump_search(arr, x):
    n = len(arr)
    jump = int(math.sqrt(n))
    prev = 0
    while arr[min(jump, n)-1] < x:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(jump, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

arr = [10, 20, 40, 50, 60, 70, 100]
x = int(input("Enter the x value: "))
result = jump_search(arr, x)
if result == -1:
    print(f"{x} Element not found in the array")
else:
    print(f"{x} Element found at index {result}")