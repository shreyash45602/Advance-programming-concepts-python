class Student:

    def __init__(self):
        self.name = ""
        self.rollno = ""

    def input(self):
        self.name = input("Enter your name: ")
        self.rollno = input("Enter your roll no: ")

    def display(self):
        print("Name =", self.name)
        print("Roll No =", self.rollno)


student1 = Student()

student1.input()
student1.display()