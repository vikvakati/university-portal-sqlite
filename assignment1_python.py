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

    def search(self):
        print("Course Search Menu: ")

    def AddDrop(self):
        print("Add Drop Menu: ")

    def printSchedule(self):
        print("Student Schedule: ")

class instructor(user):
    def __init__(self, FirstName, LastName, ID):
        super(instructor, self).__init__(FirstName, LastName, ID)

    def printSchedule(self):
        print("Instructor Schedule: ")

    def printClass(self):
        print("Class List: ")

    def search(self):
        print("Course Search Menu: ")

class admin(user):
    def __init__(self, FirstName, LastName, ID):
        super(admin, self).__init__(FirstName, LastName, ID)

    def editCatalog(self):
        print("Add or Remove Course: ")

    def editUser(self):
        print("Add or Remove User: ")

    def editClass(self):
        print("Add or Remove Student From Class List: ")

    def search(self):
        print("Course Search Menu: ")

    def printRoster(self):
        print("Select Course: ")

    def printCatalog(self):
        print("Course Catalog: ")

#test users
user1 = student("Vikranth", "Vakati", "00")
user2 = instructor("Marisha", "Rawlins", "01")
user3 = admin("John", "Doe", "02")

user1.print()
user1.AddDrop()

user2.print()
user2.printSchedule()

user3.print()
user3.editUser()


