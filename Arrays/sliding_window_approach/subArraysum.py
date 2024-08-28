def SubArraySumEqualsTarget(arr,target):
    # initialise two pointers at first index of arr
    left= 0
    right = 0
    current_sum = 0
    
    for right in range(len(arr)):
        current_sum+=arr[right]

        while current_sum > target and left <= right:
            # decreasing  left pointer value from current_sum
            current_sum -= arr[left]
            # increment left pointer to right side of array
            left +=1  

        if current_sum == target:
            return f"Target equals to sum of numbers is between indices {left} and {right}"
    return None

arr = [3,4,5,6,2,9,6]
target = 20
result = SubArraySumEqualsTarget(arr,target)
print(result)