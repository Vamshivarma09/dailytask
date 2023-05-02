# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp


# nums = [5,3,8,2,1,4]
# sort(nums)
# print(nums)

def sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[j],nums[i]=nums[i],nums[j]
    print(nums)
            
                   
nums = [5,3,8,2,1,4]

(sort(nums))

