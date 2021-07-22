class mycal:
    num=120

    def __init__(self,a,b,c):
        self.first= a
        self.second=b
        self.third=c

    def getmycall(self):
        print("here is the result")
    def summof (self):
        return self.first+ self.second + self.third + mycal.num

obj = mycal(34, 23, 45)
obj.getmycall()
print(obj.summof())
