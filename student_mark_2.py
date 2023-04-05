""" 
student:
    ID
    Name
    DOB
    Mark

course:
    ID
    Name


"""
class Student: #Enter and define student
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_mark(self, course, mark):
        self.marks.update({course: mark})

    def displayStudent(self):
        print("ID: " + self.id)
        print("name: " + self.name)
        print("DoB: " + self.dob)

    def displayMark(self, course):
        print(self.name + "'s mark: " + str(self.marks.get(course)))

class Course: #Enter and define Course
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def displayCourse(self):
        print("Course ID: " + self.id)
        print("Course name: " + self.name)
        


def numStudent():
    while True:
        try:
            NumberStudent = int(input("Enter number of student in the class: "))          
            return NumberStudent
        except ValueError:
            print("Enter again")


def studentInfo():
    studentid = input("ID: ")
    studentname = input("Name: ")
    studentdob = input("DOB: ")
    
    return studentid,studentname,studentdob


def numCourse():
    while True:
        try:
            NumberCourse = int(input("Enter number of courses: "))           
            return NumberCourse
        except ValueError:
            print("Enter again")


def courseInfo(): #Enter course information
    courseid = input("Course ID: ")
    coursename = input("Course name: ")
    
    return courseid, coursename


def findCourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Error: Invalid ID")

# def removeCourseName(course, course_id):
#     for course in course:
#         print("select to", {})

if __name__ == "__main__":
    students = []
    courses = []

    student_num = numStudent()
    print(student_num)
    for i in range(student_num):
        id, name, dob = studentInfo()
        students.append(Student(id, name, dob))

    course_num = numCourse()
    for i in range(course_num):
        id, name = courseInfo()
        courses.append(Course(id, name))

    print("Students information:\n")
    for student in students:
        student.displayStudent()

    print("Courses information:\n")
    for course in courses:
        course.displayCourse()

    
