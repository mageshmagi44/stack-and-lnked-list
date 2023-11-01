class stack:
    def __init__(self,size) -> None:
        self.size=size
        self.stack=[None]*self.size
        self.top=-1


s=stack(3)
s.stack