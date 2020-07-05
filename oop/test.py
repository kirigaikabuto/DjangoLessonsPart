#инкапсуляция защита данных и свойств от прямого воздействия
class Person:

    #конструктор
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    #getter and setters
    def getName(self):
        return self.__name

    def setName(self,name):
        if name == "hui":
            print("введит норм название")
        else:
            self.__name = name

    def setAge(self,age):
        self.__age = int(age)

    def getYear(self):
        return 2020-self.__age

p1 = Person(name="yerassyl",surname="tleugazy",age = 22)
p1.setName("hui")

print(p1.getName())
p1.setAge(23)
print(p1.getYear())
