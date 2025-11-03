# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Super() and Overriding In Classes >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
    
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
    
a = A()
b = B()
# print(b.classvar1)

# ---------------------------------------------------------------------------------------------------------------------------------------
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Operator  Overloading >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Employee:
    no_of_leaves = 8
    def __init__ (self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is (self.name). Salary is (self.salary) and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
    
    def __str__(self):
        return f"The Name is {self.name} , Salary is {self.salary} and role is {self.role}"
    
emp1 = Employee ("Harry", 35, "Programmer")
emp2 = Employee ("Rohan", 55, "Cleaner")
print(emp1 + emp2)
print(emp1 / emp2)
print(emp1)

# --------------------------------------------------------------------------------------------------------------------------------------
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Duck Typing >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# "Duck typing" = Another way to achieve polymorphism besides Inheritance
# Object must have the minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = True

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)








