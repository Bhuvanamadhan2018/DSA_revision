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

    def printNodes(self):
        current_node = self.head

        while current_node:
            print(current_node.value,end="->")
            current_node = current_node.next
        
    def findMiddleNode(self):
        slow  = self.head
        fast = self .head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.value) 
        return slow.value
my_list = linkedlist()
values = [2,3,4,5,6,7,8]
for value in values:
    my_list.insertNodes(value)

my_list.printNodes()
print('\n')

print(my_list.findMiddleNode())
        


