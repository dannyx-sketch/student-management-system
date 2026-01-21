# Student Management System

students = []

def add_student():
    name = input("Name: ")
    matric = input("Matric: ")
    dept = input("Department: ")
    level = input("Level: ")
    students.append({"name": name, "matric": matric, "department": dept, "level": level})
    print("Student added!\n")

def view_students():
    if not students:
        print("No students.\n")
        return
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} - {s['matric']} - {s['department']} - {s['level']}")
    print()  
       
def find_student(matric):
    for s in students:
        if s['matric'] == matric:
            print(f"Found: {s['name']} - {s['matric']} - {s['department']} - {s['level']}\n")
            break
        else:
            print("Not found!\n")

def update_student():
    m = input("Enter matric to update: ")
    for s in students:
        if s['matric'] == m:
            s['name'] = input("New name: ")
            s['department'] = input("New dept: ")
            s['level'] = input("New level: ")
            print("Updated!\n")
            return
    print("Not found!\n")

def delete_student():
    m = input("Enter matric to delete: ")
    for s in students:
        if s['matric'] == m:
            students.remove(s)
            print("Deleted!\n")
            return
    print("Not found!\n")

def main():
    while True:
        print("1.Add 2.View 3.Update 4.Delete 5.Exit 6.Find")
        choice = input("Choice: ")
        if choice=="1": add_student()
        elif choice=="2": view_students()
        elif choice=="3": update_student()
        elif choice=="4": delete_student()
        elif choice=="5": break
        elif choice=="6": 
            print("please enter the matric number to find the student:")
            m = input("Matric: ") 
            find_student(m)
        else: print("Invalid\n")

main()