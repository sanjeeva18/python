class new:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter"))
    def process(self):
        self.a=self.n
        while self.a!=0:
            self.r=(self.a%10)**3
            self.q=self.a//10,
            self.a=self.q
            self.sum=self.sum+self.r
    def output(self):
        if self.n==self.sum:
            print("amstrong")
        else:
            print("not")
d=new()
d.accept()
d.process()
d.output()
           

            
