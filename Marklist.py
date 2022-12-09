""" to maintain student details
roll
name
physics
chemistry
maths
computer
english
total
per
grade
"""
"""
modules imported


"""
import pickle
import os

"""
class used
"""


class student(object):
    def __int__(s):
        s.roll = 0
        s.name = " "
        s.physics = 0
        s.chemistry = 0
        s.maths = 0
        s.computer = 0
        s.english = 0
        s.total = 0
        s.per = 0
        s.grade = " "

    def add_rec(s):
        s.roll = int(input("Enter roll no: "))
        s.name = input("Enter the name: ")
        s.name = s.name.upper()
        s.physics = float(input("Enter marks of physics: "))
        s.chemistry = float(input("Enter marks of chemistry: "))
        s.maths = float(input("Enter marks of maths: "))
        s.computer = float(input("Enter marks of computer: "))
        s.english = float(input("Enter marks of english: "))
        s.total = s.physics + s.chemistry + s.maths + s.computer + s.english
        s.per = s.total / 5
        if (s.per >= 90):
            s.grade = "A1"
        elif (s.per >= 80 and s.per < 90):
            s.grade = "A2"
        elif (s.per >= 70 and s.per < 80):
            s.grade = "B1"
        elif (s.per >= 60 and s.per < 70):
            s.grade = "B2"
        else:
            s.grade = "C"

    def disp_rec(s):
        print("roll", s.roll)
        print("name", s.name)
        print("physics", s.physics)
        print("chemistry", s.chemistry)
        print("maths", s.maths)
        print("computer", s.computer)
        print("english", s.english)
        print("total", s.total)
        print("per", s.per)
        print("grade", s.grade)

    def display_rec(s):
        print("%-8s" % s.roll, "%-10s" % s.name, "%-10s" % s.physics, "%-12s" % s.chemistry, "%-10s" % s.maths,
              "%-8s" % s.computer, "%-10s" % s.english, "%-10s" % s.total, "%-10s" % s.per, "%-5s" % s.grade)
        # print("in display_rec")

    def modify_rec(s):
        s.roll = int(input("Enter new roll no"))
        s.name = input("Enter new name")
        s.name = s.name.upper()
        s.physics = float(input("Enter new marks of physics"))
        s.chemistry = float(input("Enter new marks of chemistry"))
        s.maths = float(input("Enter new marks of maths"))
        s.computer = float(input("Enter new marks of computer"))
        s.english = float(input("Enter new marks of english"))


def write_rec():
    try:
        rec = student()
        file = open("stud.dat", "ab")
        rec.add_rec()
        pickle.dump(rec, file)
        file.close()
        print("Record added in file")
        input("Press any key to cont....")
    except:
        pass


def display_all():
    os.system("cls")
    print(110 * "=")
    print("\n                                              Redi School                              \n")
    print("\n                                  LIST OF MARKS OF STUDENTS OF SCIENCE                  \n")
    print("\n                                      -Created by Kalpana Solanki                  \n")
    print("\n                                            STUDENT MARKSHEET                                     \n")
    print(110 * "=")
    try:
        file = open("stud.dat", "rb")
        print("%-8s" % "Rollno", "%-10s" % "Name", "%-10s" % "Physics", "%-14s" % "Chemistry", "%-8s" % "Maths",
              "%-10s" % "Computer", "%-10s" % "English", "%-10s" % "Total", "%-8s" % "Per", "%-5s" % "Grade")
        print(110 * "=")
        while True:
            rec = pickle.load(file)
            rec.display_rec()

    except EOFError:
        file.close()
        print(110 * "=")
        input("Press any key to cont....")
    except IOError:
        print("File could not be opened")


def search_roll():
    os.system("cls")
    try:
        z = 0
        print(110 * "=")
        print("Record searching by roll no")
        print(110 * "=")
        n = int(input("Enter roll no to search"))
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            if (rec.roll == n):
                z = 1
                print("\nRecord found and details are\n")
                rec.disp_rec()
                break

    except EOFError:
        file.close()
        if (z == 0):
            print("Record is not present")

    except IOError:
        print("File could not be opened")

    input("Press Enter to cont....")


def search_name():
    os.system("cls")
    try:
        z = 0
        n = input("Enter name to search  ")
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            if (rec.name == n.upper()):
                z = 1
                rec.disp_rec()
                break

    except EOFError:
        file.close()
        if (z == 0):
            print("Record is not present")

    except IOError:
        print("File could not be opened")

    input("Press Enter to cont....")


def modify_roll():
    os.system("cls")
    z = 0
    try:
        n = int(input("Enter roll no to modify"))
        file = open("stud.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.roll == n):
                z = 1
                print("Record found and details are")
                rec.disp_rec()
                print("Enter new data")
                rec.modify_rec()
                pickle.dump(rec, temp)
                print("Record updated")
            else:
                pickle.dump(rec, temp)

    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")

    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press Enter to cont....")


def delete_roll():
    os.system("cls")
    z = 0
    try:
        n = int(input("Enter roll no to delete: "))
        file = open("stud.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.roll == n):
                z = 1
                print("Record to delete found and details are")
                rec.disp_rec()
            else:
                pickle.dump(rec, temp)

    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")

    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press Enter to cont....")


while True:
    os.system("cls")
    print(110 * "=")
    print("""                    Main Menu
          ------------------------
          1. Add record
          2. Display all records
          3. Search by rollno
          4. Search by name
          5. Modify by rollno
          6. Delete by rollno
          7. Exit
    """)
    print(110 * "=")
    ch = int(input("Enter your choice: "))
    print(110 * "=")
    if (ch == 1):
        write_rec()
    elif (ch == 2):
        display_all()
    elif (ch == 3):
        search_roll()
    elif (ch == 4):
        search_name()
    elif (ch == 5):
        modify_roll()
    elif (ch == 6):
        delete_roll()
    elif (ch == 7):
        print("END")
        break
    else:
        print("INVALID CHOICE")