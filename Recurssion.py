#  Iterative Method 
# def steps(n):
#     for step in range(n+1):
#         print(f"Step {step}")


# Recurssion Method
# def steps(step):
#     if step == 0:
#         return
#     else: 
#         steps(step-1)
#         print(f"Step {step}")

# steps(10)


def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

n = int(input("Enter the number: "))
print(f"The factorial of {n} is {factorial(n)}")


