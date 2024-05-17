class Student:
    name: str
    age: int
    group: str
    money: int
    workhours: int
    rest = int

    def __init__(self, name, age, group, money, workhours, rest):
        self.name = name
        self.age = age
        self.group = group
        self.money = money
        self.workhours = workhours
        self.rest = rest

    def Work(self, money, workhours):
        if money <= 100:
            while money < 500:
                money = money + 10 * workhours

    def Rest(self, money, rest):
        while rest > 0:
            money = money - 50
            rest = rest - 0.5

    def printInfo(self):
        print(f'Student: {self.name}, {self.age}, {self.group}, {self.money}')

    def getInfo(self):
        return f'Student: {self.name}, {self.age}, {self.group}, {self.money}'


student1 = Student(name="PolyElly", age=113, group="C2126", money=100, workhours=4, rest=6)
student1.printInfo()
