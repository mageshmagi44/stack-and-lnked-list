class stack:
    def __init__(self,size) -> None:
        self.size=size
        self.__stack=[None]*self.size
        self.top=-1


    def push(self,value):
        if self.top==self.size-1:
            return "over flow"
        else:
            self.top+=1
            self.__stack[self.top]=value
    def pop(self):
        if self.top==-1:
            return "emppty"
        else:
            data=self.__stack[self.top]
            self.top-=1
            print(data)

    def traverse(self):
        for i in range(self.top+1):
            print(self.__stack[i],end=" ")


s=stack(4)
s.push(1)
s.push(11)
s.push(100)
s.pop()
s.pop()
s.traverse()





        