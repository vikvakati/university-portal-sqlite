#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('leopardweb.db')
print("Opened database successfully")
cursor = conn.cursor()
#sql_command = """CREATE TABLE COURSE(
#CRN INTEGER PRIMARY KEY NOT NULL,
#TITLE TEXT NOT NULL,
# department TEXT NOT NULL,
# time TEXT NOT NULL,
# days of week TEXT NOT NULL,
# semester TEXT NOT NULL,
# year INT NOT NULL,
#  credits  INT NOT NULL);"""

#sql_command = """ INSERT or IGNORE INTO COURSE VALUES( 447123, 'EMF','ECE', '11:00AM-1:00PM', 'Tuesday,Thursday', 'Summer', 2022, 4);"""
#cursor.execute(sql_command)

#sql_command = """ INSERT or IGNORE INTO COURSE VALUES(29581, 'Solid State Devices', 'ECE', '8:00 AM - 9:30 AM', 'Tuesday,Thursday', 'Summer', 2022, 3);"""
#cursor.execute(sql_command)

#sql_command = """ INSERT or IGNORE INTO COURSE VALUES(2, 'Feedback and Control', 'ECE', '2:00 PM - 3:30 PM', 'Wednesday,Friday', 'Summer', 2022, 4);"""
#cursor.execute(sql_command)


# sql_command = """ INSERT or IGNORE INTO COURSE VALUES(56757, 'ART History', 'liberal arts ', '3:30 PM - 5:30 PM', 'Monday-Wednesday', 'Summer', 2022, 4);"""
# #cursor.execute(sql_command)

# sql_command = """ INSERT or ignore INTO STUDENT VALUES(378216, 'Stephen', 'Curry', 2023, 'ME', 'CurryS');"""
# #cursor.execute(sql_command)

# sql_command = """ INSERT or ignore INTO STUDENT VALUES(365655, 'Lebron', 'James', 2022, 'EE', 'JamesL');"""
# #cursor.execute(sql_command)

# #sql_command = """DELETE FROM INSTRUCTOR where NAME = 'Joseph'"""
# #print ("Operation done successfully")

# sql_command = """ UPDATE ADMIN SET TITLE = 'Vice president' where ID = 30001 """
# #cursor.execute(sql_command)


# sql_command = """ UPDATE Course SET department = 'HUSS' where department = 'liberal arts ' """


# sql_command = """CREATE TABLE IF NOT EXISTS STUDENT_COURSE (  
# INCREMENT INTEGER PRIMARY KEY,
# CRN TEXT NOT NULL,
# ID TEXT NOT NULL)
# ;"""
# cursor.execute(sql_command) 

# sql_command = """CREATE TABLE IF NOT EXISTS INSTRUCTOR_COURSE (  
# INCREMENT INTEGER PRIMARY KEY,
# CRN TEXT NOT NULL,
# ID TEXT NOT NULL)
# ;"""
# cursor.execute(sql_command)

# #cursor.execute("DROP TABLE COURSE")

# sql_command = """CREATE TABLE IF NOT EXISTS COURSE (  
# CRN TEXT UNIQUE NOT NULL,
# TITLE TEXT NOT NULL,
# DEPARTMENT TEXT NOT NULL,
# INSTRUCTOR_FIRST TEXT NOT NULL,
# INSTRUCTOR_LAST TEXT NOT NULL,
# TIME TEXT NOT NULL,
# DAYS TEXT NOT NULL,
# SEMESTER TEXT NOT NULL,
# YEAR TEXT NOT NULL,
# CREDITS TEXT NOT NULL)
# ;"""

# cursor.execute(sql_command)



#sql_command = """INSERT OR IGNORE INTO COURSE VALUES('1000', 'APPLIED PROGRAMMING CONCEPTS', 'ELEC', 'Joseph', 'Forier', '8:00-9:50', 'MWF', 'SUMMER', 2022, 4);"""
#cursor.execute(sql_command) 

class User: #base class
	def __init__(self,first,last,id):
		self.firstname = first
		self.lastname = last
		self.ID = id

	def printFirstName(self):
		print(self.firstname)

	def printLastName(self):
		print(self.lastname)

	def printID(self):
		print(self.ID)

class instructor(User): #derived class
    def __init__(self, first, last, id):
        super().__init__(first,last,id)
    
    def printRoster(self):
        z = False
        print(self.firstname)
        while z == 0:
            print("CRN: ")
            x = input()
            cursor.execute("""SELECT INSTRUCTOR_FIRST FROM COURSE WHERE CRN = '%s' and INSTRUCTOR_FIRST = '%s' """%(x,self.firstname))
            existence = cursor.fetchall()
            if existence:
                z = 1
            else:
                z = 0
                print("That CRN is not valid or you do not teach that course ")
        print("\n Course Roster:\n")
        cursor.execute("SELECT ID FROM STUDENT_COURSE WHERE CRN= %s" "" % (x))
        id_result = cursor.fetchall()
        for i in id_result: # finds the student id of the Student_course table
            cursor.execute("SELECT NAME, SURNAME FROM STUDENT WHERE ID= %s" ""%(i))
            name_result = cursor.fetchall()
            for j in name_result: # finds the student name from Student table
                print(j)
                return name_result

    def searchCourse(self):
        print("\nCourse List: ")
        cursor.execute("""SELECT * FROM COURSE""")
        course_result = cursor.fetchall()
        for i in course_result:
            print(i)
    def searchCourseInput(self):
        print("Enter Search Parameter: ")
        x = input()
        cursor.execute("""SELECT * 
        FROM COURSE 
        WHERE CRN='%s' OR TITLE='%s' OR DEPARTMENT='%s' OR INSTRUCTOR_FIRST='%s' OR INSTRUCTOR_LAST='%s' OR TIME='%s' OR DAYS='%s' OR SEMESTER='%s' OR YEAR='%s' OR CREDITS='%s' """% (x, x, x, x, x, x, x, x, x, x))
        courseInput_result = cursor.fetchall()
        for i in courseInput_result:
             print(i)
 
class student(User):
    def __init__(self, FirstName, LastName, ID):
        super(student, self).__init__(FirstName, LastName, ID)

    def addCourse(self):
        print("CRN: ")
        x = input()
        # print("ID Number: ")
        # y = input()
        cursor.execute("""SELECT NAME 
        FROM STUDENT_COURSE
        WHERE CRN = ? and ID = ? """(x,self.ID))
        result = cursor.fetchall()
        if result:
            print("You have already added this course")
        else:
            cursor.execute("""INSERT OR IGNORE INTO STUDENT_COURSE VALUES(NULL, ?, ?)""", (x, self.ID))
            print("\nCourse Added To Schedule")

    def dropCourses(self):
        print("CRN: ")
        x = input()
        # print("ID Number: ")
        # y = input()
        cursor.execute("DELETE from STUDENT_COURSE where CRN=? AND ID =?", (x, self.ID))
        print("\n Course Deleted From Schedule")

    def searchCourse(self):
        print("\nCourse List: ")
        cursor.execute("""SELECT * FROM COURSE""")
        course_result = cursor.fetchall()
        for i in course_result:
            print(i)

    def searchCourseInput(self):
        print("Enter Search Parameter: ")
        x = input()
        cursor.execute("""SELECT * 
        FROM COURSE 
        WHERE CRN='%s' OR TITLE='%s' OR DEPARTMENT='%s' OR INSTRUCTOR_FIRST='%s' OR INSTRUCTOR_LAST='%s' OR TIME='%s' OR DAYS='%s' OR SEMESTER='%s' OR YEAR='%s' OR CREDITS='%s' """% (x, x, x, x, x, x, x, x, x, x))
        courseInput_result = cursor.fetchall()
        for i in courseInput_result:
             print(i)


class admin(User):
    def __init__(self, FirstName, LastName, ID):
        super(admin, self).__init__(FirstName, LastName, ID)

    def addCourseSystem():
        print("CRN: ")
        q = input()
        print("Course Title: ")
        r = input()
        print("Department: ")
        s = input()
        print("Instructor First Name: ")
        t = input()
        print("Instructor Last Name: ")
        u = input()
        print("Time: ")
        v = input()
        print("Days: ")
        w = input()
        print("Semester: ")
        x = input()
        print("Year: ")
        y = input()
        print("Credits: ")
        z = input()
        cursor.execute("""INSERT OR IGNORE INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (r, s, t, u, v, w, x, y, z))

        print("\n Course Added To System")

    def dropCourseSystem():
        print("CRN: ")
        x = input()
        cursor.execute("DELETE FROM COURSE WHERE CRN=%s" ""% (x))

        print("\n Course Removed From System")

    def searchCourse():
        print("\nCourse List: ")
        cursor.execute("""SELECT * FROM COURSE""")
        course_result = cursor.fetchall()
        for i in course_result:
            print(i)

    def searchCourseInput():
        print("Enter Search Parameter: ")
        x = input()
        cursor.execute("""SELECT * 
        FROM COURSE 
        WHERE CRN='%s' OR TITLE='%s' OR DEPARTMENT='%s' OR INSTRUCTOR_FIRST='%s' OR INSTRUCTOR_LAST='%s' OR TIME='%s' OR DAYS='%s' OR SEMESTER='%s' OR YEAR='%s' OR CREDITS='%s' """% (x, x, x, x, x, x, x, x, x, x))
        courseInput_result = cursor.fetchall()
        for i in courseInput_result:
             print(i)


def checkInstructorPassword(usernames, passwords): #log in for the instructor
        cursor.execute("""Select NAME,SURNAME,ID
        FROM INSTRUCTOR
        WHERE INSTRUCTOR.EMAIL = '%s' and INSTRUCTOR.ID = '%s'""" %(usernames, passwords))
        query_result = cursor.fetchall()
        z = 0
        print(z)
        for x in query_result:
            print(z)
            for y in x:
                if z == 0:
                    firstName = y
                    print(firstName)
                if z == 1:
                    lastName  = y
                    print(lastName)
                if z == 2:
                    id = y
                    print(id)
                z+=1
        if not query_result:
            return 0,0,0
        else:
            print(query_result)
            print("Welcome Instructor")
            x = 1 
            return firstName,lastName,id

def checkStudentPassword(usernames, passwords): #log in for the student
        cursor.execute("""Select NAME,SURNAME,ID
        FROM STUDENT
        WHERE STUDENT.EMAIL = '%s' and STUDENT.ID = '%s'""" %(usernames, passwords))
        query_result = cursor.fetchall()
        z = 0
        print(z)
        for x in query_result:
            print(z)
            for y in x:
                if z == 0:
                    firstName = y
                    print(firstName)
                if z == 1:
                    lastName  = y
                    print(lastName)
                if z == 2:
                    id = y
                    print(id)
                z+=1
        if not query_result:
            return 0,0,0
        else:
            print(query_result)
            print("Welcome Student")
            x = 1 
            return firstName,lastName,id

def checkAdminPassword(usernames, passwords): #log in for the admin
        cursor.execute("""Select NAME,SURNAME,ID
        FROM ADMIN
        WHERE ADMIN.EMAIL = '%s' and ADMIN.ID = '%s'""" %(usernames, passwords))
        query_result = cursor.fetchall()
        z = 0
        #print(z)
        for x in query_result:
            #print(z)
            for y in x:
                if z == 0:
                    firstName = y
                    print(firstName)
                if z == 1:
                    lastName  = y
                    print(lastName)
                if z == 2:
                    id = y
                    print(id)
                z+=1
        if not query_result:
            return 0,0,0
        else:
            print(query_result)
            print("Welcome ADMIN")
            x = 1 
            return firstName,lastName,id

def login(): # function for the log in
    print("Your username is your email")
    print("Your password is your ID number")
    userName = input("Please Enter your Username: ")
    password = input("Please Enter your Password: ") 
    return userName,password

print("Welcome to the Student Database")
z = 0
while(z == 0):
    print(" Look at the options below chose from the number 1 -3")
    print("If you are an instructor enter 1 ")
    print("If you are a student enter 2")
    print("If you are an admin enter 3")
    userInput = input("Please enter your option: ")
    print(userInput)
    if userInput not in ['1','2','3']:
        print("That input does not exist")
        inTheWorks = False
        z = 0
    else:
        z = 1
        inTheWorks = True
y = 1
while inTheWorks:
    if userInput == '1': # if user selects instructor
        username, passWord = login() #takes the tuple from the login
        firstName,lastName,id  = checkInstructorPassword(username, passWord) # Gives the attributes needed for the instructor class
        if firstName:
            # print(firstName)
            # print(lastName)
            # print(id)
            i = instructor(firstName,lastName, id) # defines the variable j which shows who the instructor is
            while(y == 1):
                print("These are the options which you have")
                print("If you want to print class  press 1")
                print(" If you want to search all Courses press 2")
                print("If you want to search courses based on parameters press 3")
                print("If you want to log out press 4")
                choice=input()
                if(choice == "1"):
                    i.printRoster()
                elif(choice == "2"):
                    i.searchCourse()
                elif(choice == "3"):
                    i.searchCourseInput()
                elif(choice == "4"):
                    y = None
                    inTheWorks = None
                else:
                    print("That number isn't valid try again")


        else:
            print("Wrong username/Password try again") # if incorrect password/username is entered
            username, passWord = login() #takes the tuple from the login
            result = checkInstructorPassword(username, passWord) # checks again to see if the  the login is incorrect
    elif userInput == '2':
        username, passWord = login() #takes the tuple from the login
        firstName,lastName,id  = checkStudentPassword(username, passWord)
        if firstName:
            s = student(firstName,lastName,id)
            while(y == 1):
                print("These are the options that you have")
                print("Add course option press 1")
                print("Drop course option press 2")
                print("Search all Courses press 3")
                print("Search by parameter press 4")
                print("Log out press 5")
                choice = input()
                if(choice == "1"):
                    s.addCourse()
                elif(choice == "2"):
                    s.dropCourses()
                elif(choice == "3"):
                    s.searchCourse()
                elif(choice == "4"):
                    s.searchCourseInput()
                    print("I have been called")
                elif(choice == "5"):
                    y = None
                    inTheWorks = None
                else:
                    print("That number isn't valid try again")
        else:
            print("Wrong username/Password try again")# if incorrect password/username is entered
            username, passWord = login() #takes the tuple from the login
            result = checkInstructorPassword(username, passWord)# checks again to see if the  the login is incorrect

    elif userInput == '3':
        username, passWord = login()
        firstName,lastName,id  = checkAdminPassword(username, passWord) #takes the tuple from the login
        if firstName:
            a = admin(firstName,lastName,id)
            while(y == 1):
                print("These are the options that you have")
                print("Add course option press 1")
                print("Drop course option press 2")
                print("Search all Courses press 3")
                print("Search by parameter press 4")
                print("Log out press 5")
                choice = input()
                if(choice == "1"):
                    a.addCourseSystem()
                elif(choice == "2"):
                    a.dropCourseSystem()
                elif(choice == "3"):
                    a.searchCourse()
                elif(choice == "4"):
                    a.searchCourseInput()
                elif(choice == "5"):
                    y = None
                    inTheWorks = None
                else:
                    print("That number isn't valid try again")
            print("Wrong username/Password try again") # if incorrect password/username is entered
            username, passWord = login() #takes the tuple from the login
            result = checkInstructorPassword(username, passWord) 
else:
        print("input doesnt exist")

            
            

conn.commit()
conn.close()

