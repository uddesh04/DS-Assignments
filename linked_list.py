class Node:  
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList:  
    def __init__(self): 
        self.head = None
  
    def detectAndRemoveLoop(self): 
        slow_p = fast_p = self.head 
        while(slow_p and fast_p and fast_p.next): 
            slow_p = slow_p.next 
            fast_p = fast_p.next.next
            if slow_p == fast_p: 
                self.removeLoop(slow_p) 
                return 1 
        return 0
  
    def removeLoop(self, loop_node): 
        ptr1 = self.head 
        while(1):  
            ptr2 = loop_node 
            while(ptr2.next != loop_node and ptr2.next != ptr1): 
             ptr2 = ptr2.next 
            if ptr2.next == ptr1 :  
             break 
              
            ptr1 = ptr1.next
        ptr2.next = None
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next
   
ll = LinkedList() 
ll.push(1) 
ll.push(56) 
ll.push(76) 
ll.push(200) 
ll.push(35)  
ll.head.next.next.next.next.next = ll.head.next.next
ll.detectAndRemoveLoop() 
print ("Linked List after removing loop")
ll.printList() 
 



#OUTPUT
#python prg3.py
#Linked List after removing loop
#35
#200
#76
#56
#10
