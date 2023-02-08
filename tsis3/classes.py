#1
class My_class:
    def __init__(self):
        self.string = input().upper()

    def printString(self):
        print(self.string)

c = My_class()
c.printString()