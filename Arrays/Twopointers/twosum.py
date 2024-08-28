def findTwoSum(arr,target):
    arr.sort() 
    left = 0
    right = len(arr)-1

    while left < right:
        if arr[left] + arr[right] == target:
           return [left,right]
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1
    return None

arr = [3,2,6,7,8,9,10]
target = 21

result = findTwoSum(arr,target)
print(result)

           