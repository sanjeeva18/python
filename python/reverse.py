class new:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.sum=self.sum*10+self.r
            self.n=self.n//10
    def output(self):
        print(self.sum)
d=new()
d.accept()
d.process()
d.output()
