class Animal:
    def __init__(self,name):
        print("it is Animal class const")
        self.name = name

    def getInfo(self):
        print("имя животного",self.name)


class Dog(Animal):
    def __init__(self,name,width):
        print("it is dog class const")
        super().__init__(name)
        self.width = width

    def getInfo(self):
        print("имя собаки",self.name)


d1 = Dog("dog1",100)
print(d1.name)
print(d1.width)
d1.getInfo()


1)принять username,password input()
2)sql=select * from users where username={username} and password={password}
data = select(sql)
if len(data)!=0:
    print("гоуу")
else:
    print("нет такого пользователя")