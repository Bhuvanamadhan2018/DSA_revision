def removeElements(arr,val):
    k = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k +=1

    return k

arr = [2,3,7,5,6,7]
val = 7
k = removeElements(arr,val)
print(arr[:k])
            

