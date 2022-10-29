class code():
    def __init__(self):
        self.a=10
    def count(self,b=12):
        self.a+=b
        print(self.a)
code=code()
code.count(6)