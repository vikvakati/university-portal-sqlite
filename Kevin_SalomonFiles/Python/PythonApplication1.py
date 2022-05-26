class User:
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


class Student(User):
	def __init__(self, first, last, id):
		super().__init__(first,last,id)
	def studentPrintFunction(self):
		print("Student function has been called\n")
class instructor(User):
	def __init__(self, first, last, id):
		super().__init__(first,last,id)
	def instructorPrintFunction(self):
		print("instructor function has been called\n")
class admin(User):
	def __init__(self, first, last, id):
		super().__init__(first,last,id)
	def adminPrintFunction(self):
		print("Admin function has been called\n")

x = Student("Kevin", "Salomon", 123456)
x.printFirstName()
x.studentPrintFunction()
y = instructor("Tom", "Brady", 1991919)
y.printLastName()
y.instructorPrintFunction()
z = admin("Lebron", "James", 1010010)
z.printLastName()
z.adminPrintFunction()

