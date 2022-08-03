import sqlite3
conn = sqlite3.connect('leopardweb.db')
print("Opened database successfully")
cursor = conn.cursor()
addcourses = """ INSERT or IGNORE INTO COURSE VALUES
(1005, 'ADVANCED MOLECULAR BIOLOGY', 'BIOL', 'Nelson', 'Patrick', '12:30 pm-01:50 pm', 'MW', 'FALL', 2022, 4),
(1006, 'ADVANCED MOLECULAR BIOLOGY-LAB', 'BIOL', 'Nelson', 'Patrick', '01:00 pm-02:50 pm', 'T', 'FALL', 2022, 0),
(1007, 'ADVANCED MOLECULAR BIOLOGY-LAB', 'BIOL', 'Nelson', 'Patrick', '10:00 am-11:50 am', 'T', 'FALL', 2022, 0),
(1008, 'STATISTICS & MECHANICS MATERIALS I', 'CIVE', 'Leonard', 'Anderson', '08:00 am-09:20 am', 'MW', 'FALL', 2022, 3),
(1009, 'MEDICAL IMAGING & OPTICS', 'BMED', 'Ronald', 'Bernier', '08:00 am-09:20 am', 'TW', 'FALL', 2022, 4),
(1010, 'MEDICAL IMAGING & OPTICS-LAB', 'BMED', 'Ronald', 'Bernier', '01:00 pm-02:50 pm', 'M', 'FALL', 2022, 0),
(1011, 'PARTIAL DIFFERENTIAL EQUATIONS', 'MATH', 'Saurav', 'Basnet', '03:30 pm-04:45 pm', 'MWF', 'FALL', 2022, 4),
(1012, '2D + 3D MEDIA & PROCESS', 'ARCH', 'Ann', 'Borst', '01:00 pm-04:50 pm', 'F', 'FALL', 2022, 4),
(1000, 'APPLIED PROGRAMMING CONCEPTS', 'ELEC', 'Joseph', 'Forier', '8:00 am-9:50 am', 'MWF', 'SUMMER', 2022, 4),
(1001, 'SENIOR DESIGN', 'ELEC', 'Patrick', 'Nelson', '10:00 am-12:50 pm', 'TR', 'SUMMER', 2022, 4),
(1002, 'CHEMISTRY', 'SCIN', 'Galilei', 'Galileo', '8:00 am-9:20 am', 'TR', 'SUMMER', 2022, 4),
(1003, 'COMPUTER NETWORKS', 'ELEC', 'Alan', 'Turing', '10:00 am-10:50 am', 'MWF', 'SUMMER', 2022, 3),
(1004, 'YOUTH DEVELOPMENT', 'HUSS', 'Katie', 'Bouman', '3:00 pm-4:50 pm', 'TR', 'SUMMER', 2022, 4);"""
cursor.execute(addcourses)
addinstructors = """ INSERT or IGNORE INTO INSTRUCTOR VALUES
(20007, 'Leonard', 'Anderson', 'Associate Professor', 1994, 'BCE', 'andersonl'),
(20008, 'Mohammed', 'Anwaruddin', 'Assistant Professor', 2010, 'BSCN', 'anwaruddinm'),
(20009, 'Tugba', 'Arsava', 'Associate Professor', 2004, 'BCE', 'arsavat'),
(20010, 'Federica', 'Aveta', 'Assistant Professor', 2009, 'BSEE', 'avetaf'),
(20011, 'Mitra', 'Bahary', 'Assistant Professor', 2005, 'BSCS', 'baharym'),
(20012, 'Payam', 'Bakhshi', 'Associate Professor', 1999, 'BSCM', 'bakhship'),
(20013, 'Saurav', 'Basnet', 'Assistant Professor', 2002, 'BSEE', 'basnets'),
(20014, 'Ronald', 'Bernier', 'Professor', 1987, 'BHU', 'bernierr1'),
(20015, 'Ann', 'Borst', 'Professor', 1983, 'BA', 'andersonl'),
(20016, 'Christopher', 'Brigham', 'Associate Professor', 2006, 'BSBE', 'brighamc2');"""
cursor.execute(addinstructors)
addstudents = """ INSERT or IGNORE INTO STUDENT VALUES
(387628, 'Matthew', 'Taylor', 2023, 'BSCO', 'taylorm6'),
(10011, 'Antonio', 'Nelson', 2023, 'BSIS', 'nelsona5'),
(10012, 'Ryan', 'Martin', 2025, 'BSEE', 'martinr2'),
(10013, 'Bob', 'Dylan', 2020, 'BFA', 'dylanb'),
(10014, 'Paul', 'Fifer', 2020, 'BSEE', 'fiferp32');"""
cursor.execute(addstudents)
print("Courses\n")
cursor.execute("""SELECT * FROM COURSE""")
course_result = cursor.fetchall()
for i in course_result:
    print(i)
print("\n")
print("Students\n")
cursor.execute("""SELECT * FROM STUDENT""")
course_result = cursor.fetchall()
for i in course_result:
    print(i)
print("\n")
print("Instructors\n")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
course_result = cursor.fetchall()
for i in course_result:
    print(i)
conn.commit()
conn.close()
