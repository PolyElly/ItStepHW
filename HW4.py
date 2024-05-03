class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')

# personX = Person(name='unknown_name', surname='unknown_surname', age=30)
# personX.info_person()

class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()


class Student(Person):
    progress: str
    group: str

    def __init__(self, progress: str, group: str, name: str, surname: str, age: int):
        self.progress = progress
        self.group = group
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_student(self):
        print(f'student:\t{self.progress} | {self.group}')

    def info_all(self):
        self.info_person()
        self.info_student()


class Work(Person):
    position: str
    duties: str

    def __init__(self, position: str, duties: str, name: str, surname: str, age: int):
        self.position = position
        self.duties = duties
        Person.__init__(name=name, surname=surname, age=age)

    def info_work(self):
        print(f'work:\t{self.position} | {self.duties}')

    def info_all(self):
        self.info_person()
        self.info_work()

teacher = Teacher(subject='Pycharm', hours=24, name='unknown_name', surname='unknown_surname', age=30)
teacher.info_all()