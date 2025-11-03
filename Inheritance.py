# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Inheritance >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 🧩 1. Single Inheritance
# A child class inherits from only one parent class.

class Parent:
    def show_parent(self):
        print("This is the Parent class")

class Child(Parent):
    def show_child(self):
        print("This is the Child class")

obj = Child()
obj.show_parent()
obj.show_child()

# ---------------------------------------------------------------------------------------------------------------------------------------
# 🧩 2. Multiple Inheritance
# A child class inherits from more than one parent class.

class Father:
    def father_traits(self):
        print("Father: Hardworking")

class Mother:
    def mother_traits(self):
        print("Mother: Caring")

class Child(Father, Mother):
    def child_traits(self):
        print("Child: Combination of both")

obj = Child()
obj.father_traits()
obj.mother_traits()
obj.child_traits()

# ---------------------------------------------------------------------------------------------------------------------------------------
# 🧩 3. Multilevel Inheritance
# A child class is derived from another child class (like a chain).

class Grandfather:
    def show_grandfather(self):
        print("Grandfather class")

class Father(Grandfather):
    def show_father(self):
        print("Father class")

class Son(Father):
    def show_son(self):
        print("Son class")

obj = Son()
obj.show_grandfather()
obj.show_father()
obj.show_son()

# ---------------------------------------------------------------------------------------------------------------------------------------

    

