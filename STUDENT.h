#pragma once
#include <iostream>
#include <string>
using namespace std;


//Class Declaration
class Student {
private: 
    //attributes
    string name;
    int age;
    int rollNo;
    float gpa;

public:
    Student(); //Default Constructor Declaration 
    Student(string n, int a, int r, float g);  //Parametrized Constructor Declaration

    ~Student();//Destructor

    //SETTER FUNCTIONS
    void setName(string n);
    void setAge(int a);
    void setRollNo(int r);
    void setGpa(float g);

    //GETTER FUNCTIONS
    string getName();
    int getAge();
    int getRollNo();
    float getGpa();

    //DISPLAY FUNCTIONS
    void displayInfo();
    void displayGrade();
};


