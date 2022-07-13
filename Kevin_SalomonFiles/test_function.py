import unittest
import myfirst
class Test_Database(unittest.TestCase):
    def test_instructorLogInWrong(self):
        actual =myfirst.checkInstructorPassword("LebronJ","99999")
        expected = 0,0,0
        self.assertEqual(actual, expected)
    def test_instructorLoginRight(self):
        actual = myfirst.checkInstructorPassword("patrickn","20002")
        expected = "Nelson","Patrick",20002
        self.assertEqual(actual,expected)
    def test_StudentLogInRight(self):
        actual = myfirst.checkStudentPassword("newton","1000")
        expected = 0,0,0
        self.assertEqual(actual,expected)
    def test_studentLoginWrong(self):
        actual = myfirst.checkStudentPassword("newtoni","10001")
        expected = "Isaac", "Newton", 10001
        self.assertEqual(actual, expected)
    def test_adminLoginWrong(self):
        actual = myfirst.checkAdminPassword("hamiltonm","30000")
        expected = 0,0,0
        self.assertEqual(actual, expected)
    def test_adminLoginRight(self):
        actual = myfirst.checkAdminPassword("hamiltonm","30001")
        expected = "Margaret", "Hamilton", 30001
        self.assertEqual(actual, expected)
    def test_PrintInstructorCourse(self):
        k = myfirst.instructor("Galileo","Galilei",20003)
        actual = k.printRoster()
        expected = "Nikola", "Tesla","Mark","Dean" 
        self.assertEqual(actual,expected)
if __name__ == '__main__':
    unittest.main()