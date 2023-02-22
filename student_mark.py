def input_StudentList(info):
    num_student = input("Enter number of students: ")
    num = int(num_student)
    while num > 0:
        id = input("Student's ID: ")
        if not is_exist(info, id):
            name = input("Student's name: ")
            dob = input("DOB: ")
            student = [name, dob]
            info[id] = student
            num = num - 1
        else:
            print("This id existed.")
    

def input_CourseList(info):
    num_of_course = input("Enter number of course : ")
    num = int(num_of_course)
    while num > 0:
        id = input("Course's ID : ")
        if not is_exist(info, id):
            name = input("Course's name : ")
            course = [name]
            info[id] = course
            num = num - 1
        else:
            print("This id existed.")
    

CourseList = {}
StudentList = {}
Mark = {}
def list_student():
    print("{:10} | {:20} | {:20}".format("ID", "Name", "DOB"))
    for key in StudentList:
        print("{:10} | {:20} | {:20}".format(key, StudentList[key][0], StudentList[key][1]))


def list_course():
    print("{:10} | {:12}".format("ID", "Name"))
    for key in CourseList:
        print("{:10} | {:12}".format(key, CourseList[key][0]))


def list_Mark():
    i = 0
    print("{:10} | {:20} | {:10}".format("ID", "Name", "Mark"))
    for key in Mark:
        name = str(Mark[key][i][i])
        mark = str(mark[key][i][i + 1])
        print("{:10} | {:20} | {:10}".format(key, name, mark))


def add_mark_to_course(course_mark, student, course):
    input_course = input("Enter course's ID: ")
    for mark in course:
        if mark == input_course:
            course_mark[input_course] = []
            for key in student:
                student_mark = input(f"Input student {key} / {student[key][0]}'s mark: ")
                course_mark[input_course].append([student[key][0], student_mark])
            break
        if mark not in course:
            print("Please try again!")


end = False
def is_empty(dictionary):
    if len(dictionary) == 0:
        return True
    return False
def is_exist(dictionary, id):
    if id in dictionary:
        return True
    return False



while not end:   
    choice = input("Enter 1 to start: ")
    if choice == "1":
        input_StudentList(info=StudentList)
        input_CourseList(info=CourseList)
        empty = is_empty(StudentList)
        if not empty:
            list_student()
        else:
            print("There are no students in class!")
        empty = is_empty(CourseList)
        if not empty:
            list_course()
        else:
            print("There are no courses!")
        add_mark_to_course(Mark, StudentList, CourseList)
        empty = is_empty(Mark)
        if not empty:
            list_Mark()
        else:
            print("There are no courses have mark!")
    
    else:
        print("{choice} is an invalid input!")