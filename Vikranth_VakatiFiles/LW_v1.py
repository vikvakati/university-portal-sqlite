import sqlite3

# database file connection 
database = sqlite3.connect("assignment3.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

#SQL command to create a table in the database 
sql_command = """CREATE TABLE IF NOT EXISTS COURSE (  
CRN TEXT UNIQUE NOT NULL,
TITLE TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL,
INSTRUCTOR_FIRST TEXT NOT NULL,
INSTRUCTOR_LAST TEXT NOT NULL,
TIME TEXT NOT NULL,
DAYS TEXT NOT NULL,
SEMESTER TEXT NOT NULL,
YEAR TEXT NOT NULL,
CREDITS TEXT NOT NULL)
;"""
cursor.execute(sql_command) 

sql_command = """CREATE TABLE IF NOT EXISTS STUDENT_COURSE (  
INCREMENT INTEGER PRIMARY KEY,
CRN TEXT NOT NULL,
ID TEXT NOT NULL)
;"""
cursor.execute(sql_command) 

sql_command = """CREATE TABLE IF NOT EXISTS INSTRUCTOR_COURSE (  
INCREMENT INTEGER PRIMARY KEY,
CRN TEXT NOT NULL,
ID TEXT NOT NULL)
;"""
cursor.execute(sql_command) 
 
#remove table
#cursor.execute("DROP TABLE INSTRUCTOR_COURSE")

class user:
#Set functions for each attribute
    def __init__(self, FirstName, LastName, ID):
        self.f = FirstName
        self.l = LastName
        self.id = ID

#Function to print all info for the object
    def print(self):
        print("Name: ", self.f, self.l, "\nID: ", self.id)

#subclasses
class student(user):
    def __init__(self, FirstName, LastName, ID):
        super(student, self).__init__(FirstName, LastName, ID)

    def addCourse():
        print("CRN: ")
        x = input()
        print("ID Number: ")
        y = input()
        cursor.execute("""INSERT OR IGNORE INTO STUDENT_COURSE VALUES(NULL, ?, ?)""", (x, y))
        print("\nCourse Added To Schedule")

    def dropCourse():
        print("CRN: ")
        x = input()
        print("ID Number: ")
        y = input()
        cursor.execute("DELETE from STUDENT_COURSE where CRN=? AND ID =?", (x, y))
        print("\n Course Deleted From Schedule")

    def searchCourse():
        print("\nCourse List: ")
        cursor.execute("""SELECT * FROM COURSE""")
        course_result = cursor.fetchall()
        for i in course_result:
            print(i)

class instructor(user):
    def __init__(self, FirstName, LastName, ID):
        super(instructor, self).__init__(FirstName, LastName, ID)

    def printRoster():
        print("CRN: ")
        x = input()

        print("\n Course Roster:\n")

        cursor.execute("SELECT ID FROM STUDENT_COURSE WHERE CRN=%s" ""% (x))
        id_result = cursor.fetchall()
        for i in id_result:
            cursor.execute("SELECT NAME, SURNAME FROM STUDENT WHERE ID=%s" ""% (i))
            name_result = cursor.fetchall()
            for j in name_result:
                print(j)

    def searchCourse():
        print("\nCourse List: ")
        cursor.execute("""SELECT * FROM COURSE""")
        course_result = cursor.fetchall()
        for i in course_result:
            print(i)

class admin(user):
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


#https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
ans=True
while ans:
    print("""
		1. Add a Course (student)
		2. Remove a Course (student)
		3. Print Course Roster (instructor)
		4. Add Course to System (admin)
		5. Remove Course from System (admin)
		6. Exit/Quit
	""")
	
    ans = input("Select An Action: \n")

    if ans=="1":
        student.addCourse()
	
    elif ans=="2":
        student.dropCourse()
	
    elif ans=="3":
        instructor.printRoster()

    elif ans=="4":
        admin.addCourseSystem()
	
    elif ans=="5":
        admin.dropCourseSystem()
	
    elif ans=="6":
        student.searchCourse()

    elif ans=="7":
        print("\n Goodbye") 
        ans = None
    
    else:
        print("\n Not Valid Choice Try again")

database.commit() 
  
# close the connection 
database.close() 