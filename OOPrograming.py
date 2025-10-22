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

        