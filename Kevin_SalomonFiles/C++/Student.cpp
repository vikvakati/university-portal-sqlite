// Student.cpp
#include "User.h"
#include "Student.h"
#include <iostream>
#include <string>
using namespace std;

//constructor
student::student(string f, string l, int i)
	:User{ f,l,i }
{
	cout << "constructor for the student has been called" << endl;
}

// student print
void student::printStudent()
{
	cout << "the student function been called" << endl;
}

//student
student::~student()
{
	cout << "Destructor for the student has been called" << endl;
}
