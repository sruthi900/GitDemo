from Classes import Calculator1


class B:
    def __init__(self):
        self.db= Calculator1(3,5)
    def getdata1(self):
        self.db.getdata()

obj6=B()
obj6.getdata1()
