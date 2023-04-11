
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next:
            new_node.next.prev=new_node

    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node    
        

    def print_list(self,node):
        print("\n Traversal in forward direction.")
        while node:
            print(node.data,end=" ")
            last=node
            node=node.next
        print("\n Traversal in reverse direction.", end=" ")
        while last:
            print(last.data,end=" ")
            last=last.prev

#driver code

if __name__=="__main__":
    llist=DoublyLinkedList()
#    llist.append(6)
    llist.push(7)
    llist.push(1)
#    llist.append(4)
    llist.insert_after(llist.head.next,8)
    print(" Created DLL is : ",end=" ")
    llist.print_list(llist.head)

    
            
        
