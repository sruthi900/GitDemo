from Classes import Calculator1


class ChildImp(Calculator1):
    num2=300
    def __init__(self):
        Calculator1.__init__(self,2,10)


    def getcompletedata(self):
        return self.num2+self.num+self.summation()

obj5=ChildImp()
print(obj5.getcompletedata())
