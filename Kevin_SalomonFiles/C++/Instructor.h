#pragma once
#include <string>
#ifndef INSTRUCTOR_H
#define INSTRUCTOR_H
#include "User.h"

class instructor : public User {
public:
	instructor(std::string,std::string,int);
	void printInstructor();
	~instructor();
};
#endif

