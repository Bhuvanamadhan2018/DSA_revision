def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    k = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[k]= nums[i]
            k +=1

    return k
#  k represents no.of unique elements

nums = [2,3,4,5,6,6,7]
k = removeDuplicates(nums)
print(k)
print(nums[:k])

# Time Complexity = O(n) , n is length of input array
# Space Complexity = O(1)
        