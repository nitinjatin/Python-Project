#Q1 
# dict_ionary = {
#     "किसान" : "Farmer",
#     "उदाहरण" : "Example",
#     "आग" : "Fire",
#     "भारत" : "India",
#     "सरकार" : "Government"}

# lookup_value = input("Enter the word you want to find... ")
# print(dict_ionary[lookup_value])
# print(dict_ionary.get(lookup_value))

#Q2
# num_1 = int(input("Enter the First number: "))
# num_2 = int(input("Enter the Second number: "))
# num_3 = int(input("Enter the Third number: "))
# num_4 = int(input("Enter the Fourth number: "))
# num_5 = int(input("Enter the Fifth number: "))
# num_6 = int(input("Enter the Sixth number: "))
# num_7 = int(input("Enter the Seventh number: "))
# num_8 = int(input("Enter the Eight number: "))

# Set_1 = {num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8}
# print(Set_1)
# print(type(Set_1))

# Q3
# set_1 = {
#     18 , "18"            #So,Yes We can have 18 as int and "18" as string.
# }
# print(set_1)    


# Q4 
# s = {20,20.0,"20"}         # So, We have 2 in output. 
# But equality (==) compares values, not types. When Python compares an int and a float, it converts the int to a float internally:
# print(len(s))

#Q5
# s = {}
# print(type(s))              #T's dictionary

# Q6
# dict_1 = {}
# f = 1 
# while f<=4:
#     n = input("Enter Your Name: ")
#     l = input("Enter your favorite language: ")
#     dict_1.update({n:l})
#     f+=1
# print(dict_1)

# Q7,Q8
# dict_1 = {
#     "Nitin" : "Hindi",
#     "Nitin" : "Hindi",
#     "Zoro" : "Hindi",
#     "Nitin" : "Japanese",
#     "Jinwoo" : "Korean",
#     "Cha hae" : "Korean"
# }
# print(dict_1)
#Thus, Values can be same but key or identifier should be unique otherwise it will show you updated version of key's.

# Q9
# Can you change the values inside a list which is Contained in Set.
# s = {8,7, 12, "Harry", [1,3]}
# No, Sets in Python can only contain immutable (hashable) elements. Lists are mutable,so they cannot be added in sets


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>