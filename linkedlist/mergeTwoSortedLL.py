class ListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def  mergeTwoSortedlinkedlist(ListA,ListB):
    fake_node = ListNode(0)
    current_node = fake_node 
    while ListA and ListB:
        if ListA.val < ListB.val:
            current_node.next = ListA
            ListA = ListA.next
        else:
            current_node.next = ListB
            ListB = ListB.next
    current_node = current_node.next

    if ListA:
        current_node.next = ListA
    if ListB:
        current_node.next = ListB

    return fake_node.next

ListA = ListNode(1)
ListA.next = ListNode(2)
ListA.next.next = ListNode(4)
ListA.next.next.next = ListNode(6)
ListA.next.next.next.next = ListNode(8)

ListB = ListNode(1)
ListB.next = ListNode(5)
ListB.next.next = ListNode(7)
ListB.next.next.next = ListNode(9)
ListB.next.next.next.next = ListNode(8)

result = mergeTwoSortedlinkedlist(ListA,ListB)
print(result)
