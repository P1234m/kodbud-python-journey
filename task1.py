#Task 1 :
'''Explanation: Create a command-line calculator that performs:
•
Addition, subtraction, multiplication, division
•
Takes user input using input()
•
Uses if-else conditions for operations
Goal: Practice basic syntax and user input/output.'''
print("Simple CLI Calculator")
num1=float(input("Enter first number: "))
operator=input("Enter operation (+,-,*,/): ")
num2=float(input("Enter second number: "))

#Performing the operation and returning the result

if operator=='+':
    print("Result: ",num1+num2)
elif operator=='-':
    print("Result: ",num1-num2)
elif operator=='*':
    print("Result: ",num1*num2)
elif operator=='/':
    print("Result: ",num1/num2)
else:
    print("Invalid operator")