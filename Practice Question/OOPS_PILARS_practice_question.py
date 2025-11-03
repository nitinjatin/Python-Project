# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  HARRY CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1

class Two_D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def define(self):
        vector = [self.x,self.y]
        print(f"{vector}\nList With Two elemnets is 2D Vector")

    def __str__(self):
        return f"vector{self.x,self.y}\nList With Three elemnets is 2D Vector"


class Three_D(Two_D):
    def __init__(self,x,y,z):
        super().__init__(x,y)          # reuse parent constructor
        self.z = z

    def define(self):
        vector = [self.x,self.y,self.z]
        print(f"{vector}\nList With Three elemnets is 3D Vector")

    def __str__(self):
        return f"vector{self.x,self.y,self.z}\nList With Three elemnets is 3D Vector"


list_1 = Two_D(2,3)
list_2  = Three_D(5,6,7)
# list_1.define()
# list_2.define()
# print(list_1)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Q2

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("Dog is barking...")

# finn = Dog()
# finn.bark()

# ---------------------------------------------------------------------------------------------------------------------------------------

# Q3

class Employee():
    def __init__(self,salary):
        self._salary = salary
    
    @property
    def salary(self):
        return f"Your new Salary is : {self._salary}"
    
    @salary.setter
    def salary(self,new_salary):
        if new_salary >= 15000 and new_salary <=30000:
            self._salary = new_salary*0.4+new_salary
        elif new_salary >= 30000 and new_salary <=50000:
            self._salary = new_salary*0.5+new_salary
        elif new_salary >= 50000 and new_salary <=650000:
             self._salary = new_salary*0.55+new_salary
        elif new_salary >= 65000 and new_salary <=850000:
            self._salary = new_salary*0.60+new_salary
        elif new_salary > 850000:
            self._salary = new_salary*0.66+new_salary
        else:
            print("Not Eligible For Increment..")

# emp_1 = Employee(40000)
# emp_1.salary = 45000
# print(emp_1.salary)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Q4

class complex():
    
    def __init__(self,real,imaginory):
        self.real = real
        self.imaginory = imaginory

    def __add__(self , num2):
        new_real = self.real + num2.real
        new_img = self.imaginory + num2.imaginory
        return complex(new_real,new_img)

    def __str__(self):
        return f"{self.real} + {self.imaginory}"
    
num1 = complex(4,6)
num2 = complex(4,6)

num3 = num1+num2
print(num3)

# ---------------------------------------------------------------------------------------------------------------------------------------

