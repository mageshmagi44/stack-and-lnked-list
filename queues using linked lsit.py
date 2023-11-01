class node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self,data):
       newnode=node(data)
       if self.rear==None:
          self.front=self.rear=newnode
       else:
          self.rear.next=newnode
          self.rear=newnode

    def dequue(self):
       if self.front==None:
          return "queue is empty"
       else:
          self.front=self.front.next

    def isempty(self):
       return self.front==None
    
    def size(self):
       curr=self.front
       count=0
       while curr:
          count+=1
          curr=curr.next
       print(count)
       
        

    def traverse(self):
       curr=self.front
       while curr:
          print(curr.data,end=" ")
          curr=curr.next
  
s=Queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.dequue()
s.enqueue(10)
s.size()
s.traverse()