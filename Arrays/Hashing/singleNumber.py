def singlenumber(arr):
    hash_map = {}
    for i in arr:
        if i in hash_map:
            hash_map[i] += 1
        hash_map[i] = 1
    for key in hash_map:
        if hash_map[i] == 1:
            return key
        
arr = [2,6,7,4,2,6,7]
result = singlenumber(arr)
print(result)

