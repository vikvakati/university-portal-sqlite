#pragma once
#include<string>
#ifndef USER_H
#define USER_H

class User
{
public:
	User(std::string,std::string,int);
	void setFirstName(std::string);
	std::string getFirstName() const;
	void setLastName(std::string);
	std::string getLastName() const;
	void setID(int);
	int getID() const;
	~User();
protected:
	std::string firstName;
	std::string lastName;
	int ID;
};
#endif