class new:
    def __init__(self):
        self.c=1
        self.f=1
    def accept(self):
        self.n=int(input("enter1"))
    def process(self):
        for i in range(1,self.n+1):
            self.f=self.c*self.f
            self.c=self.c+1
            print(self.f)
d=new()
d.accept()
d.process()

