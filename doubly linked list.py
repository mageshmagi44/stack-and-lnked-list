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
        