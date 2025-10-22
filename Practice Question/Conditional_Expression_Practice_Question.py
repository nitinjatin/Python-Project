# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< APNA COLLEGE  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Q1 Write a program to check number entered by user is odd or an even?
# input_number = int(input("Enter the number you want to check: "))

# if input_number%2 == 0:
#     print(f"{input_number} is even number")
# else:
#     print(f"{input_number} is odd number")

# Q2 Write a program to find the greatest of 3 numbers entered by the user?
# input_number_1 = int(input("Enter the First Number: "))
# input_number_2 = int(input("Enter the Second Number: "))
# input_number_3 = int(input("Enter the Third Number: "))
# input_number_4 = int(input("Enter the Fourth Number: "))

# if input_number_1>input_number_2 and input_number_1 > input_number_3:
#     print(f"{input_number_1} is the greatest amongst " )
# elif input_number_2 > input_number_1 and input_number_2>input_number_3:
#     print(f"{input_number_2} is the greatest amongst ")
# elif input_number_3 > input_number_1 and input_number_3>input_number_2:
#     print(f"{input_number_3} is the greatest amongst ")


# Q3 Write a program to find the greatest of 4 numbers entered by the user?
# a = int(input("Enter the First Number: "))
# b = int(input("Enter the Second Number: "))
# c = int(input("Enter the Third Number: "))
# d = int(input("Enter the Fourth Number: "))

# if a>=b and a>=c and a>=d:
#     print(f"{a} is largest number")
# elif b>=a and b>=c and b>=d:
#     print(f"{b} is largest number")
# elif c>=a and a>=b and a>=d:
#     print(f"{a} is largest number")
# else:
#     print(f"{d} is largest number")


# Q4 Write a program to check if  a number is multiple of 7or not?
# input_number = int(input("Enter the number which is multiple of 7 or not: "))

# if input_number%7 == 0:
#     print(f"{input_number} is multiple of 7")
# else:
#     print(f"{input_number} is not multiple of 7")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HARRY CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Q2
# english = int(input("Enter English Marks: "))
# hindi = int(input("Enter Hindi Marks: "))
# math = int(input("Enter Math Marks: "))
# total_marks = (english+hindi+math)

# if (english/100)<0.30:
#     print("You have failed in English")
# if (hindi/100)<0.30:
#     print("You have failed in Hindi")
# if (math/100)<0.30:
#     print("You have failed in Math")

# if (total_marks/300)<0.40:
#     print("You have failed (less than 40%)")
# else:
#     print("Congrats....")
#     print("You have passed in all subjects")

# Q3
# comment = input("Enter Your Comment: ")

# if comment.__contains__("Make a lot of money") == True:
#     print("Spam Detected...")
# elif comment.__contains__("buy now") == True:
#     print("Spam Detected...")
# elif comment.__contains__("subscribe this") == True:
#     print("Spam Detected...")
# elif comment.__contains__("click this") == True:
#     print("Spam Detected...")
# else:
#     print("Comment Added...")

# Q4
# username = input("Please Enter your username: ")

# if len(username) < 10:
#     print("Please Retry..")
#     print("Username should be at least 10 characters")
# else:
#     print("Congrats...")
#     print("Your Username is added...")

# Q5
# list_1 = ["Bob","Shaw","Oliver","Finn","Jack","Kerry","Charlie"]
# check_name = input("Enter Name you want to check: ")

# if list_1.__contains__(check_name) == True:
#     print("Your Entered name is in the list...")
# else:
#     print("Your Entered name is not in the list...")

# Q6
# std_name = input("Enter your name: ")
# std_marks = int(input("Enter Your Marks: "))

# if std_marks >= 90:
#     std_grd = "Experience"
# elif std_marks >= 80:
#     std_grd = "A-grade"
# elif std_marks >= 70:
#     std_grd = "B-grade"
# elif std_marks >= 60:
#     std_grd = "C-grade"
# elif std_marks >= 50:
#     std_grd = "D-grade"
# elif std_marks <50 :
#     std_grd = "Fail"

# print(f"Dear {std_name},\nYour are {std_grd}")

# Q7
# post = input("Enter your post: ")

# if "harry" in post.lower():
#     print("This post is talking about harry")
# else:
#     print("This post is not talking about harry")
