class display:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter a numbetr"))
    def process(self):
        for i in range(1,self.n):
            if self.n%i==0:
                print(i)
                self.sum=self.sum+i
    def output(self):
        if self.sum==self.n:
            print("perfect")
        else:
            print("no")
d=display()
d.accept()
d.process()
d.output()
