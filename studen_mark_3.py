from math import *


class Student:
    def __init__(self, id="", name="", dob="", GPA=0):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__GPA = GPA

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def getGPA(self):
        return self.__GPA

    def setGPA(self, GPA):
        self.__GPA = GPA

    def input(self):
        self.__id = input("Enter Student Id: ")
        self.__name = input("Enter Student Name: ")
        self.__dob = input("Enter Student Date of Birth: ")

    def __str__(self):
        return "ID: " + self.__id + " Student: " + self.__name + " DOB: " + self.__dob

    def describe(self):
        print(self.__str__())


class Mark:
    def __init__(self, studentName, course, mark=0, cetc=0, GPA=0):
        self.__studentName = studentName
        self.__course = course
        self.__etc = etc
        self.__mark = mark
        self.__GPA = GPA

    def input(self):
        print(f"Enter Student's mark for {self.__studentName}")
        self.__mark = float(input(f"in {self.__course}: "))
        self.__etc = Course.getetc(course)

    def getMark(self):
        return floor(self.__mark * 10) / 10

    def getCourse(self):
        return self.__course

    def getGPA(self):
        return floor(self.__GPA * 10) / 10

    def setGPA(self, GPA):
        self.__GPA = GPA

    def getName(self):
        return self.__studentName

    def getCredit(self):
        return self.__etc

    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self, id="", name="", etc=0):
        self.__id = id
        self.__name = name
        self.__etc = etc

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCredit(self):
        return self.__etc

    def input(self):
        self.__id = input("Enter Course Id: ")
        self.__name = input("Enter Course Name: ")
        self.__etc = int(input("Enter etc : "))

    def __str__(self):
        return "Course: " + self.__name + " with id of " + self.__id + " and credit of " + str(self.__etc)

    def describe(self):
        print(self.__str__())



ClassRoom = []
ListOfCourse = []
Marks = []

# find the number of students
NumberStd = int(input("Enter number of Students: "))

# adding Student objects into array ClassRoom
for i in range(NumberStd):
    s = Student()
    s.input()
    ClassRoom += [s]

# print out all the students in ClassRoom
for student in ClassRoom:
    print(student)

# find the number of courses
NumberOfCourse = int(input("Enter number of Courses: "))

# print out all the courses in ListOfCourse
for c in ListOfCourse:
    print(c)


# choose a course
def choseCourse():
    Course = input("Enter the course name: ")
    return Course


# input marks for all student in a Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == ListOfCourse[i].getName():
            for j in range(NumberStd):
                m = Mark(ClassRoom[j].getName(), ListOfCourse[i].getName(), ListOfCourse[i].getCredit())
                m.input()
                Marks.append(m)


# average Mark
def averageMark(Name):
    x = y = 0
    for mark in Marks:
        if mark.getName() == Name:
            x += mark.getMark() * mark.getCredit()
            y += mark.getCredit()

    AverageMark = x / y
    AverageMark_fld = floor(AverageMark * 10) / 10
    print("Average Mark for " + Name + ": " + str(AverageMark_fld))

    for students in ClassRoom:
        if students.getName() == Name:
            students.setGPA(AverageMark_fld)

