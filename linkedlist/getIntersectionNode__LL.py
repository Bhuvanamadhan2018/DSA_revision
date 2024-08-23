class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

def getIntersectionNode(headA,headB):
    new_set = set()
    current_node = headA
    
    while current_node:
        new_set.add(current_node)

        current_node = current_node.next

    current_node = headB

    while current_node:
        if current_node in new_set:
            return current_node
        current_node = current_node.next
    
    return None

headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)
headA.next.next.next.next.next = ListNode(6)

headB = ListNode(7)
headB.next = ListNode(5)
headB.next.next=ListNode(4)
headB.next.next.next=ListNode(9)
headB.next.next.next.next = headA.next.next.next.next = ListNode(5)

result = getIntersectionNode(headA,headB)
print(result.value)

