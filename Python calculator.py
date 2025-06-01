#python calculator

operator=input("Enter operator(+,-,*,/): ")

num1= float(input("Enter the first operand: "))
num2= float(input("Enter the second operand: "))

if operator=="+":
    result=num1+num2
    print(f"Result: {round(result,1)}")
elif operator=="-":
   result= num1-num2
   print(f"Result: {round(result,1)}")
elif operator=="*":
  result=num1*num2
  print(f"Result: {round(result,1)}")
elif operator=="/":
   result= num1/num2
   print(f"Result: {round(result,1)}")
else:
    print("Invalid input, Thank you!")
