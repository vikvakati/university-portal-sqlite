import sqlite3
conn = sqlite3.connect('leopardweb.db')
print("Opened database successfully")
cursor = conn.cursor()
addcourses = """ INSERT OR IGNORE INTO COURSE VALUES
(1005, 'ADVANCED MOLECULAR BIOLOGY', 'BIOL', 'Nelson', 'Patrick', 'FALL', 2022, 4, '12:30PM', '1:50PM', 'YES', 'NO', 'YES', 'NO', 'NO'),
(1006, 'ADVANCED MOLECULAR BIOLOGY-LAB', 'BIOL', 'Nelson', 'Patrick', 'FALL', 2022, 0, '1:00PM', '2:50', 'NO', 'YES', 'NO','NO', 'NO'),
(1007, 'ADVANCED MOLECULAR BIOLOGY-LAB', 'BIOL', 'Nelson', 'Patrick', 'FALL', 2022, 0, '10:00AM', '11:50AM', 'NO', 'YES','NO', 'NO', 'NO'),
(1008, 'STATISTICS & MECHANICS MATERIALS I', 'CIVE', 'Leonard', 'Anderson', 'FALL', 2022, 3, '8:00AM', '9:20AM', 'YES', 'NO','YES', 'NO', 'NO'),
(1009, 'MEDICAL IMAGING & OPTICS', 'BMED', 'Ronald', 'Bernier', 'FALL',  2022, 4, '8:00AM', '9:20AM', 'NO', 'YES','YES', 'NO', 'NO'),
(1010, 'MEDICAL IMAGING & OPTICS-LAB', 'BMED', 'Ronald', 'Bernier', 'FALL', 2022, 0, '1:00PM', '2:50PM', 'YES', 'NO','NO', 'NO','NO'),
(1011, 'PARTIAL DIFFERENTIAL EQUATIONS', 'MATH', 'Saurav', 'Basnet', 'FALL', 2022, 4, '3:30PM', '4:45PM', 'YES', 'NO','YES', 'NO', 'YES'),
(1012, '2D + 3D MEDIA & PROCESS', 'ARCH', 'Ann', 'Borst', 'FALL', 2022, 4, '1:00PM', '4:50PM', 'NO', 'NO','NO', 'NO', 'YES'),
(1000, 'APPLIED PROGRAMMING CONCEPTS', 'ELEC', 'Joseph', 'Forier', 'SUMMER', 2022, 4, '8:00AM', '9:50AM', 'YES', 'NO','YES', 'NO', 'YES'),
(1001, 'SENIOR DESIGN', 'ELEC', 'Patrick', 'Nelson', 'SUMMER', 2022, 4, '10:00AM', '12:50PM', 'NO', 'YES','NO', 'YES', 'NO'),
(1002, 'CHEMISTRY', 'SCIN', 'Galilei', 'Galileo', 'SUMMER', 2022, 4, '8:00AM', '9:20AM', 'NO', 'YES','NO', 'YES', 'NO'),
(1003, 'COMPUTER NETWORKS', 'ELEC', 'Alan', 'Turing', 'SUMMER', 2022, 3, '10:00AM', '10:50AM', 'YES', 'NO','YES', 'NO', 'YES'),
(1004, 'YOUTH DEVELOPMENT', 'HUSS', 'Katie', 'Bouman', 'SUMMER', 2022, 4, '3:00PM', '4:50PM', 'NO', 'YES','NO', 'YES', 'NO');"""
cursor.execute(addcourses)
addinstructors = """ INSERT OR IGNORE INTO INSTRUCTOR VALUES
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
addstudents = """ INSERT OR IGNORE INTO STUDENT VALUES
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
