# Student Management System (SMS)

## Student Infomation
Name:Ayeleso Inioluwa Daniel

Course:Sen201

Matric No:24/13842

Department:Computer Science

## Project Overview
The **Student Management System (SMS)** is a Python console application designed to manage student records efficiently. The system allows users to:  
- Add new students  
- View all students  
- Update student information
- Find (search) a student by matric number 
- Delete student records  

This project also demonstrates the **complete Software Development Life Cycle (SDLC)** using consistent function names and clear design.

---

## Software Development Life Cycle (SDLC) Phases

### 1. Requirement Analysis
**Functional Requirements:**  
- Add, view, update, and delete student records.  

**Non-Functional Requirements:**  
- Easy-to-use console interface  
- Runs on any machine with Python installed  
- Temporary in-memory storage (no database required)  

---

### 2. System Design
- Each student is stored as a **dictionary** with keys: `name`, `matric`, `department`, `level`.  
- All students are stored in a **list** called `students`.  
- Main functions of the system:
  - `add_student()` → Add a new student  
  - `view_students()` → View all students
  - `find_student()` → Find a student by matric number
  - `update_student()` → Update an existing student  
  - `delete_student()` → Delete a student  
  - `main()` → Menu-driven controller  

---

### 3. Implementation
- Developed in **Python**  
- Console-based, menu-driven interface  
- Beginner-friendly code, easy to maintain  

---

### 4. Testing
- Tested all functionalities:
  - Adding students  
  - Viewing students
  - Finding students
  - Updating records  
  - Deleting records  
- Confirmed that all features work as expected without errors  

---

### 5. Deployment
To run the system:  
1. Save the Python file as `student_management_system.py`  
2. Open your terminal or command prompt  
3. Navigate to the folder containing the file  
4. Run the command:

---

### 6. Maintenance & Future Improvements
- Save student records to a file or database
- Add login authentication for security
- Develop a GUI for better usability
```bash

python student_management_system.py

