// admin.cpp
#include "User.h"
#include "Admin.h"
#include <iostream>
#include <string>
using namespace std;

//constructor
admin::admin(string f, string l, int i)
	:User{ f,l,i }
{
	cout << "constructor for the admin has been called" << endl;
}

// admin print
void admin::printAdmin()
{
	cout << "the instructor function been called" << endl;
}

//destructor
admin::~admin()
{
	cout << "Destructor for the admin has been called" << endl;
}
