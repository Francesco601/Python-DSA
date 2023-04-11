
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedQueue:

    def __init__(self):
        self.head=None
        self.tail= None

    def is_empty(self):
        return self.head == None

   
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            answer=self.head.data
            self.head=self.head.next
            if self.is_empty():
                self.tail=None
        return answer     

    def enqueue(self,e):
        newest=Node(e)
        if self.is_empty():
            self.head=newest
            
        else:
            self.tail.next= newest
        self.tail= newest    
      
               
if __name__=="__main__":
    q=LinkedQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)       
    q.enqueue(50)

    q.dequeue()

    print("\n Queue head: " + str(q.head.data if q.head != None else -1))
    print("\n Queue tail: " + str(q.tail.data if q.tail != None else -1))      

     

            
            
        
    
