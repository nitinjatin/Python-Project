# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< APNA COLLEGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1 Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

class student():

    # print("Welcome To Database....\n")

    def __init__(self,name,marks_of_english,marks_of_math,marks_of_hindi):
        self.name = name
        self.marks_of_english = marks_of_english
        self.marks_of_hindi = marks_of_hindi
        self.marks_of_math = marks_of_math
        print(f"Student Name: {name}\nStudent Marks of english: {marks_of_english}\nStudent Marks of hindi: {marks_of_hindi}\nStudent Marks of math: {marks_of_math}")
    
    def avg_method(self):
       avg_marks = (self.marks_of_math+self.marks_of_english+self.marks_of_hindi)/3
       print(f"Average of Student: {avg_marks}")
       print("")

# std_1 = student("Jerry",45,44,67)
# std_1.avg_method()
# std_2 = student("Dora",75,54,57)
# std_2.avg_method()


# Q2 Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class account():

    # Welcome = "Welcome To Python Bank"
    # print(Welcome)

    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
        print(f"Dear Customer,\nYour Account number. is: {account_no}\nYour Available Balance is: {balance} ")
    
    def debit(self,amount):
        self.balance -= amount
        print(f"A/c{self.account_no} debited INR {amount}.\nRemaining Balance: {self.balance}")
    
    def credit(self,amount):
        self.balance += amount
        print(f"A/c{self.account_no} credited INR {amount}.\nRemaining : {self.balance}")
    
# customer_1 = account(8000 , "PB3456390")
# customer_1.debit(2000)
# customer_1.credit(2000)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HARRYCODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1

class programmer():
    # greet = "\t\t\tWelcome to Microsoft"
    # print(greet)

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        print(f"Programmer Name: {name}\nProgrammer language: {language}\nProgrammer Salary: {salary}\n")


# programmer_1 = programmer("Fin","Python",1200000)
# programmer_2 = programmer("George","C++",2200000)

# Q2

import math
class calculator():
    # greet = "\t\t\t\tWELCOME TO PYTHON CALCULATOR"
    # print(greet)

    def square(self,num):
        print(num*num)

    def cube(self,num):
        print(num*num*num)
    
    def Square_root(self,num):
        print(math.sqrt(num))
    
# calculator().square(4)
# calculator().cube(4)
# calculator().Square_root(4)
    
# Q3 Create a class with a class attribute a; create an object from it and set ‘a’directly using ‘object.a = 0’. Does this change the class attribute?

class ques():
    a = 1

# Prints the class attribute because instance attribute is not present
# object = ques()                    
# print(object.a)

# Instance attribute is set
# object.a = 0
# print(object.a)            # Prints the instance attribute because instance attribute is present

# Prints the class attribute
# print(ques().a)

# Q5

class train():
    greet = "\t\t\t\tWELCOME TO INDIAN RAILWAYS"
    print(greet)

    def __init__(self,name,mobile_no,from_to_station,gender,preferred_class,train_no):
        self.name = name
        self.mobile_no = mobile_no
        self.from_to_station = from_to_station
        self.gender = gender
        self.prepreferred_class =preferred_class
        self.train_no = train_no

    def book_ticket(self):
        print("Confirming Your Details....")
        print(f"Dear Passenger,\nYour train no : {self.train_no}\nYour Name : {self.name}\nYour mobile no. : {self.mobile_no}\nYour destination : {self.from_to_station}\nYour gender : {self.gender}\nYour class : {self.prepreferred_class}")
        print("HAPPY JOURNEY")
    
    def get_status(self):
        if self.train_no == 22436:
            print(f"Available Seats are : {45}")
        elif self.train_no == 12302:
            print(f"Available Seats are : {33}")
        elif self.train_no == 22120:
            print(f"Available Seats are : {23}")

    def get_info(self):
        if self.train_no == 22436:
            print("Route: Varanasi Junction (BSB) – New Delhi (NDLS)\nType: Semi-high-speed express train operated by Indian Railways.\nDetails you can see:\nDeparture time: 15:00 hrs from Varanasi\nArrival time: 23:00 hrs at New Delhi\nJourney time: 8 hours\nRunning days: All days except Monday and Thursday\nLive status: You can check it at enquiry.indianrail.gov.in or ixigo.com/trains")
        elif self.train_no == 12302:
            print("Route: New Delhi (NDLS) – Howrah Junction (HWH)\nType: Premium high-speed, long-distance express train.\nDetails you can see:\nDeparture: 16:55 hrs from New Delhi\nArrival: 10:55 hrs the next day at Howrah\nClasses available: 1AC, 2AC, 3AC\nMeals included in ticket fare\nLive running status available on NTES or RailYatri.")
        elif self.train_no == 22120:
            print("Route: Karmali (GOA) – Mumbai Chhatrapati Shivaji Maharaj Terminus (CSMT)\nType: Modern semi-high-speed corporate train.\nDetails you can see:\nDeparture: 15:00 hrs from Karmali\nArrival: 23:00 hrs at Mumbai\nOnboard Wi-Fi, LCD display, automatic doors\nReal-time updates at railmitra.com or NTES.")
    
passenger_1 = train("Raju","989896554","Varanasi to Delhi","Male","Sleeper",22436)
# passenger_1.book_ticket()
# passenger_1.get_status()
# passenger_1.get_info()
