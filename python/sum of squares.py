class num:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.sum=self.sum+(self.r**2)
            self.n=self.n//10
    def output(self):
        print(self.sum)
d=num()
d.accept()
d.process()
d.output()
            
