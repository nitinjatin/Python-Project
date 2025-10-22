#python program to add two numbers
'''
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

print("Result Is :", a+b )
'''

#python program to find remainder when divided by 
'''
c = int(input("Enter the no: "))
d = int(input("Enter the no: "))
print("Result Is :", c % d )
'''

#python program to find data type of a variable
import ast
# Import the Abstract Syntax Trees module
input_number = input("Enter the data you want to check its data: ")

try:
    evaluated_data = ast.literal_eval(input_number) # Safely evaluate the input string
    b = type(evaluated_data)
    print("The data type of this :" , b)

except ValueError: # If it can't be evaluated, it's just a string
    print("the type of your data is plain string: ")


print(type(input("enter the character  ")))
