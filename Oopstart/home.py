class Home:

    def __init__(self, a1, b1, c):
        self.a = a1
        self.b = b1
        self.array = c

    def appendToArray(self, number):
        self.array.append(number)

    def getSumOfArray(self):
        sumi = 0
        for i in self.array:
            sumi = sumi + i
        return sumi

    def printArray(self):
        for i in self.array:
            print(i,end=" ")
        print("\n")

    def getArea(self):
        return self.a * self.b

    def getPerimeter(self):
        return 2*(self.a+self.b)


