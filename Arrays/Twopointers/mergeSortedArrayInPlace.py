def mergeSortedArray(nums1,m,nums2,n):
    lastIndex1 = m-1
    lastIndex2 = n-1
    finalMergedArray = m+n-1

    while lastIndex1>=0 and lastIndex2>=0:
        if nums1[lastIndex1] > nums2[lastIndex2]:
              nums1[finalMergedArray] = nums1[lastIndex1]
              lastIndex1 -=1

        else:
             nums1[finalMergedArray] = nums2[lastIndex2]
             lastIndex2 -=2
        finalMergedArray -=1
        # copy remaining elements from nums2 into the merged array
        while lastIndex2>=0:
             nums1[finalMergedArray] = nums2[lastIndex2]
             lastIndex2 -=1
             finalMergedArray -=1
        

nums1 = [1,2,3,4,5,6]
m = 3
nums2 = [7,8,9,10]
n = 3
mergeSortedArray(nums1,m,nums2,n)
print(nums1)

# Time Complexity = O(m+n)
# Space Complexity = O(1), as we're modifying nums1 in place