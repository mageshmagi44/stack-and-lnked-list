class node:
    def __init__(self,data,next=None) -> None:
        self.data=data
        self.next=next

class stack:
    def __init__(self) -> None:
        self.top=None

    def isempty(self):
        return self.top==None
    
    def push(self,data):
        newnode=node(data)
        newnode.next=self.top
        self.top=newnode

    def peek(self):
        if (self.isempty()):
            return "stack is empty"
        else:
            return self.top.data
        
    def pop(self):
        if (self.isempty()):
            return "stackis empty"
        else:
            self.top =self.top.next



    def traverse(self):
        curr=self.top
        while curr:
            print(curr.data)

            curr=curr.next
    def size(self):
        return len(self.data)


class linked_list:
    def __init__(self) -> None:
        self.head=None


    def prepend(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode


    def append(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            return
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode


    def atmid(self,after,data):
        newnode=node(data)
        current=self.head
        while current!=None:
            if current.data==after:
                break
            current=current.next

        if current!=None:
            newnode.next=current.next
            current.next=newnode

        else:
            print("item notfound")
    def clear(self):
        self.head=None
    def del_head(self):
        if self.head==None:
            return "linked list is empty"
        else:
            self.head=self.head.next

    def del_tail(self):
        if self.head==None:
            print("empty")

        if self.head.next==None:
            return self.del_head()
        
        current=self.head
        while current.next.next!=None:
            current=current.next
        current.next=None
    def delbyval(self,val):
        if self.head==None:
            return "empty linked lsit"
        if self.head.data==val:
            return self.del_head()
        current=self.data
        while current.next:
            if current.next.data==val:
                break
            current=current.next
        if current.next==None:
            return "not found"
        else:
            current.next=current.next.next
    def searchbyval(self,item):
        current=self.head
        pos=0
        while current:
            if current.data==item:
                return pos
            current=current.next
            pos+=1
        return" not found"
    
    def searchbyindex(self,index):
        current=self.head
        pos=0
        while current:
            if pos==index:
                return current.data
            current=current.next
            pos+=1

        return "out"
    
    def traverse(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next













machaaaaaaa







































def tarverse(self):
    current=self.head
    while current:
        print(current.data,end="-->")
        current=current.next        



a=stack()
a.push(1)
a.push(2)
a.push(3)
print(a.peek())


