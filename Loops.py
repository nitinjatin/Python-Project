# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FOR AND WHILE LOOPS WITH BREAK AND CONTINUE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# i = 0 
# while i < 10:
#     print("🍀","🦚")
#     i+=1

# for o in range(1,11):
#     print(o)

# i = 1
# while i <=10:
#     print(i)
#     if i == 3:
#         break           # It instructs the program to - Exit the loop now.
#     i+=1

# for i in range(1,11):
#     print(i)
#     if i ==3 :
#         break


# i = 1
# while i <= 10:
#     print(i)
#     i+=1
#     if i == 3:
#         i+=1
#         continue        # It instructs the program to "Skip the specific iteration"


# for i in range(1,11):
#     if i == 3:
#         continue
#     print(i)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< NESTED LOOPS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# for i in range(1,5):
#     for q in range (1,6):
#         print(q)
#     print("")


#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Ques) Check the prime number in range >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
# start = int(input("Enter the number you want to start: "))
# end  = int(input("Enter the number you want to end: "))

# for i in range (start,end):
#     if i == 0 or i == 1:
#         print("Not Prime","---",i)
#     else:    
#         for q in range (2,i):
#             if i%q == 0:
#                 print("Not Prime","---",i)
#                 break
#         else:
#             print("Prime Number","---",i)



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Ques) Check the entered number is prime or not >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# num = int(input("Enter the number you want to check: "))
# if num == 1 or num == 0:
#     print("This is not Prime number... ")
       
# else:
#    for i in range(2,num):
#       if num%i == 0 :
#         print("This is not Prime number... ")
#         break
#    else:
#       print("This is Prime number... ")
     

