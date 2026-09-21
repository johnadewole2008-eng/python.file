#a simple python calculator
operator=input("enter an operator(+,-,*,/): ")
num1= int(input("enter 1st number:"))
num2= int(input("enter 2nd number:"))
if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    result=num1/num2
    print(result)
else:
    print(f"{operator} is an invalid operator")