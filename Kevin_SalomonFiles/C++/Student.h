#pragma once
#include <string>
#ifndef STUDENT_H
#define STUDENT_H
#include "User.h"

class student : public User {
public:
	student(std::string,std::string,int);
	void printStudent();
	~student();
};
#endif

