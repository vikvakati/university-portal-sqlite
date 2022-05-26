#include "User.h"
#include "Student.h"
#include "Admin.h"
#include "Instructor.h"
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
	cout << "Welcome to the Database" << endl;
	instructor k{ "Kevin","Salomon",123456 };
	k.printInstructor();
	admin j{ "Lebron","James",123876 };
	j.printAdmin();
	student m{ "Venus","Williams",187677 };
	m.printStudent();
	cout << "bye" << endl;
	return 0;
}