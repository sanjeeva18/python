class new:
    def __init__(self):
        self.c=1
        self.f=1
    def accept(self):
        self.n=int(input("enyter"))
    def process(self):
        while self.c<=self.n:
            self.f=self.c*self.f
            self.c=self.c+1
            print(self.f)
d=new()
d.accept()
d.process()

