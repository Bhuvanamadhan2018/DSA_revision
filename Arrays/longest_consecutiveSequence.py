def longestConsecutiveSequence(arr):
    arr.sort()
    longest_sequence = 0
    current_sequence = 1
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1] == 1:
            current_sequence +=1
        else:
            
            longest_sequence = max(longest_sequence,current_sequence)
            current_sequence = 1
    return f"Longest Consecutive Sequence is:{max(longest_sequence,current_sequence)}"


arr = [5,3,45,6,7,8,10,9,3,4,2,20,22,26]
res = longestConsecutiveSequence(arr)
print(res)
    