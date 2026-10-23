import pickle

class Student:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.id = ""

    def createStudent(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.id = input("Enter your ID: ")

    def displayStudent(self):
        print(self.name)
        print(self.age)
        print(self.id)

myStudentsList = []

while True:
    print("1. Add a Student")
    print("2. Display Student")
    print("3. Exit")
    print("4. Clear file")

    choice = input("Enter your choice: ")
    if choice == "3":
        print("Exiting...")
        break

    elif choice == "1":
        stu = Student()
        stu.createStudent()
        myStudentsList.append(stu)

        file1 = open("myStudents.dat","ab")
        pickle.dump(stu,file1)
        file1.close()

    elif choice == "2":
            file2 = open("myStudents.dat","rb")

            while True:
                try:
                    data = pickle.load(file2)
                    data.displayStudent()


                except EOFError:
                    break

            file2.close()

    elif choice == "4":
        input("Press 'enter' to clear: ")
        file3 = open("myStudents.dat", "wb")
        file3.close()


