# 🎓 Student Information System (SIS) — C++ OOP Prototype

A simple **Object-Oriented Programming (OOP)** prototype built in **C++** for managing basic student information.  
This project demonstrates key OOP principles such as **encapsulation**, **abstraction**, **constructors**, **destructors**, and **constructor overloading**.

---

## 🧠 Project Overview

You have recently joined **TechVision Pvt. Ltd.** as a Junior Software Developer.  
Your task: build a small prototype of a **Student Information System (SIS)** that can store and manage basic student records.

The system represents real-world entities (students) as C++ classes and objects, showing how OOP helps organize data efficiently.

---

## 🚀 Features

✅ **Encapsulation** — Data members (`name`, `age`, `rollNo`, `gpa`) are private; access controlled through getters and setters.  
✅ **Abstraction** — Methods like `displayGrade()` hide internal GPA-to-grade logic.  
✅ **Constructors** — Both default and parameterized constructors demonstrate object initialization flexibility.  
✅ **Destructor** — Displays a message when an object is destroyed, showing object lifecycle.  
✅ **Constructor Overloading** — Multiple constructors with different parameters.  
✅ **Clear, Simple, and Modular** — Code split across `.h`, `.cpp`, and `main.cpp` files.

---



---

## 💻 Code Summary

### Class: `Student`

| Member | Type | Description |
|---------|------|-------------|
| `name`  | `string` | Student's name |
| `age`   | `int` | Student's age |
| `rollNo` | `int` | Unique roll number |
| `gpa` | `float` | Grade Point Average |

**Public Methods**
- `setName(string)`, `setAge(int)`, `setRollNo(int)`, `setGpa(float)` — setters  
- `getName()`, `getAge()`, `getRollNo()`, `getGpa()` — getters  
- `displayInfo()` — prints all attributes  
- `displayGrade()` — calculates and prints letter grade (A–F)

**Constructors**
- `Student()` — default constructor  
- `Student(string, int, int, float)` — parameterized constructor

**Destructor**
- `~Student()` — prints a message when object is destroyed

---





