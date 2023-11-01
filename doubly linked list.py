class node:
    def __init__(self,data) -> None:
        self.data=data
        self.nref=None
        self.pref=None

class doublyll:
    def __init__(self) -> None:
        self.head=None

    def traverse(self):
        if self.head==None:
            return "empty likedlist"
        n=self.head
        while n:
            print(n.data,"-->",end=" ")
            n=n.nref
    def revtraverse(self):
        print()
        if self.head==None:
            return "empty ll"
        n=self.head
        while n.nref:
            n=n.nref
        while n:
            print(n.data,"-->",end=" ")
            n=n.pref
    def insert_empty(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            print("ll is not empty")

    def prepend(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode
    def append(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            n=self.head
            while n.nref!=None:
                n=n.nref
            n.nref=newnode
            newnode.pref=n

    def add_after(self,data,after):
        if self.head==None:
            print("linked list is empty")
        else:
            curr=self.head
            while curr:
                if curr.data==after:
                    break
                curr=curr.nref
            if curr is None:
                print("notfound")
            else:
                newnode=node(data)
                newnode.nref=curr.nref
                newnode.pref=curr
                if curr.nref is not None:
                    curr.nref.pref=newnode
                curr.nref=newnode
    def add_before(self,data,before):
        if self.head==None:
            print("linked list is empty")
        else:
            curr=self.head
            while curr:
                if curr.data==before:
                    break
                curr=curr.nref
            if curr is None:
                print("notfound")
            else:
                newnode=node(data)
                newnode.nref=curr
                newnode.pref=curr.pref
                if curr.pref!=None:
                    curr.pref.nref=newnode
                else:
                    self.head=newnode
                curr.pref=newnode




d=doublyll()
d.append(100)
d.append(1000)
d.prepend(10)
d.prepend(1)
d.add_after(90,10)
d.add_before(2,10)
d.traverse()
d.revtraverse()
