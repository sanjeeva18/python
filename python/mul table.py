class new:
    def accept(self):
        self.n=int(input("enter1"))
    def process(self):
        c=1
        while c<=10:
            self.a=c*self.n
            c=c+1
            print(self.a)
d=new()
d.accept()
d.process()
