#pragma once
#include <string>
#ifndef ADMIN_H
#define ADMIN_H
#include "User.h"

class admin : public User {
public:
	admin(std::string, std::string,int);
	void printAdmin();
	~admin();
};
#endif
