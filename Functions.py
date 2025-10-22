def avg():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    print(f"The Average is {(round((a+b+c/3),0))}")
    return f"Average is {(round((a+b+c/3),0))}"


avg()
print(avg())

