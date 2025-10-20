#include "Student.h"


//DEFAULT CONSTRUCTOR USED
Student::Student() {
    name = "Unknown";
    age = 0;
    rollNo = 0;
    gpa = 0.0;
}

//PARAMETRIZED CONSTRUCTOR USED

Student::Student(string n, int a, int r, float g) {
    name = n;
    age = a;
    rollNo = r;
    gpa = g;
}

//DESTRUCTOR USAGE
Student::~Student() {
    cout << "Destructor called for " << name << endl;
}

//SETTER FUNCTION FOR NAME
void Student::setName(string n) { 
    name = n;
}

//SETTER FUNCTION FOR AGE
void Student::setAge(int a) {
    age = a; 
}

//SETTER FUNCTION FOR SET ROLL NO
void Student::setRollNo(int r) { 
    rollNo = r; 
}

//SETTER FUNCTION FOR GPA
void Student::setGpa(float g) {
    gpa = g; 
}

//GETTER FUNCTION FOR NAME
string Student::getName() {
    return name;
}

//GETTER FUNCTION FOR AGE
int Student::getAge() {
    return age; 
}

//GETTER FUNCTION FOR ROLL NO
int Student::getRollNo() {
    return rollNo; 
}

//GETTER FUNCTION FOR GPA
float Student::getGpa() {
    return gpa; 
}


// FUNCTION FOR DISPLAYING
void Student::displayInfo() {
    cout << "Name: " << name << "\nAge: " << age << "\nRoll No: " << rollNo << "\nGPA: " << gpa << endl;
}

//FUNCTION FOR DISPLAYING GRADE
void Student::displayGrade() {
    if (gpa >= 3.6)
        cout << "Grade: A" << endl;
    else if (gpa >= 3.1)
        cout << "Grade: B" << endl;
    else if (gpa >= 2.0)
        cout << "Grade: C" << endl;
    else
        cout << "Grade: F" << endl;
}
