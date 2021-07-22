from OopsConstructor import calculator


class childimp(calculator):
    num2=585

    def __init__(self):
        calculator.__init__(self, 54, 24)
    def getcompldata(self):
        return self.num + self.num2 + self.summation()

obj = childimp()
print(obj.getcompldata())