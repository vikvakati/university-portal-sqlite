#include "User.h"
#include <string>
#include <iostream>
using namespace std;

//constructor
User::User(string f,string l, int i)
{
	firstName = f;
	lastName = l;
	ID = i;

	cout << "Constructor called for User" << endl;
}

//setfirstName
void User::setFirstName(string f)
{
	firstName = f;
}

//getFirstname
string User::getFirstName() const
{
	return firstName;
}

// set last name
void User::setLastName(string l)
{
	lastName = l;
}

//get last name
string User::getLastName() const
{
	return lastName;
}

//set ID
void User::setID(int i)
{
	ID = i;
}

//get ID
int User::getID() const
{
	return ID;
}

//destructor
User::~User()
{
	cout << "Destructor has been called for User" << endl;
}