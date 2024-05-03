class StudySubject:
    name: str
    hours: int
    enable: bool

    def __init__(self, name: str, hours: int, enable: bool):
        self.name = name
        self.hours = hours
        self.enable = enable

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')


python = StudySubject(name='Python', hours=18, enable=True)


# python.info_study()

class Student:
    name: str
    surname: str
    study: StudySubject

    def __init__(self, name: str, surname: str, study: StudySubject):
        self.name = name
        self.surname = surname
        self.study = study

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        self.study.info_study()


student = Student(name='uknown_name', surname='unknow_surname', study=python)
student.info_all()
