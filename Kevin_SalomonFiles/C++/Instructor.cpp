// instructor.cpp
#include "User.h"
#include "Instructor.h"
#include <iostream>
#include <string>
using namespace std;

//constructor
instructor::instructor(string f, string l, int i)
	:User{f,l,i}
{
cout << "constructor for the instructor has been called" << endl; 
}

// instructor print
void instructor::printInstructor()
{
	cout << "the instructor function been called" << endl; 
}

//destructor
instructor::~instructor()
{
	cout << "Destructor for the instructor has been called" << endl;
}
