class new():
    def __init__(self):
        self.c=2
        self.r=1
    def input(self):
        self.n=int(input())
    def process(self):
        while self.c<=self.n/2:
            self.r=self.n%self.c
            self.c=self.c+1
        if self.r!=0:
            print("primr")
        else:
            print("no")
d=new()
d.input()
d.process()
