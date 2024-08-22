class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
            
    def insertNodes(self,value):
        new_node = ListNode(value)
        
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    def printNodes(self):
        current_node = self.head

        while current_node:
            print(current_node.value,end='->')
            current_node = current_node.next

        # print "None" at end if the linked list
        print(current_node)
    def findMiddleOfLL(self):
        current_node = self.head
        count = 0
        while current_node:
            count+=1
            current_node = current_node.next
        middle_node = self.head
        for _ in range(1,count//2+1):
            middle_node = middle_node.next
        print(f"The middle node is:",middle_node.value)
        # return middle_node.value


values =[4,5,7,9,2,3]
mylist = LinkedList()
for value in values:
    mylist.insertNodes(value)
mylist.findMiddleOfLL()


