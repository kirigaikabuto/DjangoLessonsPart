class Person:

    #конструктор
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    #метод который сробатывает при выводе объекта
    def __str__(self):
        return self.name+" "+self.surname

p1 = Person(name="yerassyl",surname="tleugazy")
p1.name="hui"
print(p1.name)
print(p1.surname)

# класс -> чертеж дома
# объет -> дом


# int
# string
# char
# float
# double