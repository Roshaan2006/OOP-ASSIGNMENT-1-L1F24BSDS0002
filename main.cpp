#include "Student.h"
#include<iostream>


int main() {
    cout << "-------------------------\n";

    //FIRST OBJECT USING SETTER METHODS
    Student s1;
    s1.setName("Roshaan");
    s1.setAge(20);
    s1.setRollNo(0002);
    s1.setGpa(3.9);
    s1.displayInfo();
    s1.displayGrade();
    cout << endl;
    cout << "-------------------------\n";

    //SECOND OBJECT USING PARAMETRIZED CONSTRUCTOR
    Student s2("Ahmad", 21, 0003, 3.2);
    s2.displayInfo();
    s2.displayGrade();
    cout << endl;
    cout << "-------------------------\n";

    //THIRD OBJECT ALSO USING PARAMETRIZED CONSTRUCTOR
    Student s3("Bilawal", 20, 0004, 2.1);
    s3.displayInfo();
    s3.displayGrade();
    cout << endl;
    cout << "-------------------------\n";

    //FOURTH CONSTRUCTOR USING DEFAULT CONSTRUCTOR
    Student s4;
    s4.displayInfo();
    s4.displayGrade();
    cout << endl;


    //DEMO FOR GETTER METHODS 
    cout <<"-----------------------------------";
    cout << "\nTop Student: " << s1.getName() << " (GPA: " << s1.getGpa() << ")" << endl;
    cout <<"-----------------------------------\n";

    return 0;
}
