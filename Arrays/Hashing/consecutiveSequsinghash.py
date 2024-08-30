def longest_consecutive_sequence(arr):
    num_set = set(arr)
    longest = 0
    for i in num_set:
        if i-1 not in num_set:
            length = 1
             
            while i + length in num_set:
                length +=1
            longest = max(longest,length) 
    return longest

arr = [31,2,3,5,4,599,89]
print(longest_consecutive_sequence(arr))
        
