class Student:
    name: str
    age: int
    group: str
    money: int

    work = 4

    def __init__(self, name, age, group, money):
        self.name = name
        self.age = age
        self.group = group
        self.money = money

    def printInfo(self):
        print(f'Student: {self.name}, {self.age}, {self.group}, {self.money}')

    def getInfo(self):
        return f'Student: {self.name}, {self.age}, {self.group}, {self.money}'


student1 = Student(name="PolyElly", age=113, group="C2126", money='work')
student1.printInfo()


#print(student1.getInfo())