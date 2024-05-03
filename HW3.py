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


# subjects = StudySubject(name=input("Subject: "), hours=int(input("Hours: ")), enable=True)
# python.info_study()

subject = StudySubject(name=input("Subject: "), hours=int(input("Hours: ")), enable=True)
# now how do we put it in list


class Student:
    name: str
    surname: str
    study: list[StudySubject]

    def __init__(self, name: str, surname: str, study: StudySubject):
        self.name = name
        self.surname = surname
        self.study = [study]

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        self.study.info_study()


student = Student(name=input("Name: "), surname=input("Surname: "), study=subject)
student.info_all()
