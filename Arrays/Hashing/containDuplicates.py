def containDuplicates(arr):
    hash_map = {}
    for i in  arr:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] +=1
            return True
    return False

arr = [2,1,4,5,6]
result = containDuplicates(arr)
print(result)