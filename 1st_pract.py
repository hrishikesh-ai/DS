class Student:
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name

    def dekho(self):
        return f"Your Name is {self.name} and Roll No is {self.roll}" 
    


a = input("Enter roll no :")
b = input("Enter name :")

student = Student(a,b)
print(student.dekho())