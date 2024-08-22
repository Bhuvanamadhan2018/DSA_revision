class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def insertNodes(self,value):
        new_node = ListNode(value)

        if not self.head:
            self.head  = new_node 
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node 

    
    def createCycle(self)->ListNode:
        head = current_node = self.head
        second_node = head.next.next

        while current_node.next:
            current_node = current_node.next

        current_node = second_node

        return current_node
    
def listHasCycle(head)->bool:
    fast = head
    slow = head
    while fast and fast.next:
        slow =  slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False



# def printNodes(head: ListNode):
#         current_node = head

#         while current_node:
#             print(current_node.value,end="->")
#             current_node = current_node.next

mylist = linkedlist()
values = [2,4,5,6,7,8]
for value in values:
    mylist.insertNodes(value)
print('\n')

cycledlist=mylist.createCycle()

result = listHasCycle(cycledlist)
print(result,"has cycle")