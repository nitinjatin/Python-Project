# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< <<< APNA COLLEGE QUESTION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Q1) Search for a number x in this tuple using loop:
# t = (1,4,9,16,25,36,49,64,81,100)
# find = int(input("Enter the number you want to find: "))
# index = 0

# for i in t:
#     if i == find:
#         print("Entered number available in tuple")
#         print("Available at Index No: ",index)
#         break
#     index+=1
# else:
#     print("Number not available in tuple...")


# Q2) Print the multiplication table of a number n
# n = int(input("Enter the number you want to mulptiple: "))

# for i in range(1,11):
#     print(n*i)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HARY CODE QUESTION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Q2
# list_1 =["Harry","Sohan","Sachin","Rahul"]
# i = 0
# while i < len(list_1):
#     if list_1[i].__contains__("S") == True:
#         print("Good Morning,",list_1[i])
#     i+=1


# Q3
# num = int(input("Enter The number you want to multiply: "))
# i = 1
# while i <=10:
#     print(num*i)
#     i+=1


# Q4
# num = int(input("Enter the number you want to check whether is prime or not: "))
# if num == 0 or num == 1:
#     print("The Entered number is not prime... ")

# else:
#     for i in range(2,num):
#         if num%i == 0:
#             print("The Entered number is not prime... ")
#             break
#     else:
#         print("The Entered number is Prime number...")


# Q5
# n = int(input("Enter the number: "))
# i = 1
# sum = 0

# while i<=n:
#     print(i)
#     sum = i+sum
#     i+=1
# print("Sum of first n numbers = ",sum)

# Q6
# n = int(input("Enter the number: "))
# product = 1

# for i in range(1,n+1):
#     print(i)
#     product = i*product
# print("The Factorial or product of given number are =" , product)

# Q7
# k = 1
# g = 2
# for i in range(1,4):
#     for j in range(g):
#         print(" ",end=" ")
#     for q in range(k):
#         print("*",end=" ")
#     k+=2
#     g-=1
#     print("")

# Q8
# for i in range(1,4):
#     for q in range(i):
#         print("*",end=" ")
#     print(" ")


# <<<<<<<<<<<<< Dynamic rectangle >>>>>>>>>>>>>>
# while(True):
#     n = int(input("Enter Range: "))
#     for i in range(1,n):
#         for q in range(1,n):
#             if i == 1 or q == 1 or i == n-1 or q == n-1:
                
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print(" ")


# Q9
# for i in range(1,4):
#     for q in range (1,4):
#         if i == 2 and q == 2:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print(" ")


# Q10
# n = int(input("Enter the multiplication number: "))
# for i in range(10, 0, -1):
#     print(n*i, end = " ")

  
