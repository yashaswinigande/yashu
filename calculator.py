number1=input("enter the num")
num1=int(number1)
sign=input('enter the sign')
number2=input('enter the number')
num2=int(number2)
if sign=='+':
    print('your result is',str(num1+num2))
elif sign=='-':
    print("your result is",str(num1-num2))
elif sign=='*':
    print("your result is",str(num1*num2))
elif sign=='/':
    if num2 != 0:
        print("your result is",str(num1/num2))
    else:
        print("Error: Division by zero is not allowed.")
elif sign=='%':
    if num2 != 0:
        print("your result is",str(num1 % num2))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
