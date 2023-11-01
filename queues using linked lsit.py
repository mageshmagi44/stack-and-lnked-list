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
          self.front=newnode=self.rear

    def traverse(self):
       curr=self.front
       while curr:
          print(curr.data,end=" ")
          curr=curr.next
  
