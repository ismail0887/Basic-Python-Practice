#self keyword is mandotory to calling veriable name in method
#instance & class variable have whole different purpose
#construction name should be __init__

class calculator:
    num= 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("m executing methods in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + calculator.num


obj = calculator(2,4)     #syntax to create object in python
obj.getdata()
print(obj.summation())

obj1 = calculator(4,6)
obj1.getdata()
print(obj1.summation())
