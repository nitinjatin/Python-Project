class student:
    def __init__(self , name , english_marks , math_marks , science_marks):
        self.name = name
        self.english_marks = english_marks
        self.math_marks = math_marks
        self.science_marks = science_marks

    def average(self):
        print(f"The average of student {self.name} is {round(self.english_marks + self.math_marks + self.science_marks / 3)}")

std_1 = student("Rohan" , 89 , 77 , 90)
std_2 = student("Roy" , 49 , 87 , 80)

std_1.average() 
std_2.average()
print(std_1.name)
print(student.average(std_1))
print(std_1.average())
'''
In Python, methods and functions have similar purposes but differ in important ways.
Functions are independent blocks of code that can be called from anywhere like print() or type(),
while methods are tied to objects or classes and need an object or class instance to be invoked.
'''

class Test:
    a = 1


obj1 = Test()
obj2 = Test()

obj1.a = 5      # Creates instance attribute on obj1
print(obj1.a)   # 5 (instance)
print(obj2.a)   # 1 (class)
print(Test.a)   # 1 (class)

Test.a = 9      # Changes class attribute
print(obj1.a)   # 5 (instance still unchanged)
print(obj2.a)   # 9 (class changed)
print(Test.a)   # 9
      

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def info(self):
        print(self.name,self.marks)

stu1 = Student("Nitin", 95)
# stu1.marks = -10   # ❌ Directly modified — invalid marks
# Student.marks = 90
print(stu1.marks)
# stu1.info()
# print(Student.marks)
