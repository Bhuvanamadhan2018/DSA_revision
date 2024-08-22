def reverseWordsInLinkedList(s):
    res = s.strip().split()
    left = 0
    right = len(res)-1

    while left < right:
        res[left] , res[right] = res[right] , res[left]
        left +=1
        right -=1
    return " ".join(res)

s = "  hello  word! "
result = reverseWordsInLinkedList(s)
print(result)
