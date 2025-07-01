#self jeyword is mandatory for calling variable names intomethod
#constructor name shoud be init
#new keyword is not required wen you create object
#Instance and class variable have diff purpose

class Calculator1:
    num=300
    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print("i am called automatically when an object is crested")
    def getdata(self):
        print("i am called when an method is created")
    def summation(self):
         print("summing two numbers")
         return self.firstNumber+self.secondNumber+self.num

obj1=Calculator1(2,3)
obj1.getdata()
print(obj1.summation())

obj2=Calculator1(6,7)
obj2.getdata()
obj2.summation()










