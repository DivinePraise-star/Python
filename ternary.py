#ternary operator

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
Age=int(input("Enter age: "))

print("Positive" if num1>0 else "Negative")
print("Even number" if num1%2==0 else "Odd number")
print("Positive" if num2>0 else "Negative")
print("Even number" if num2%2==0 else "Odd number")
print(f"{num1} is the maximum number" if num1>num2 else num2)
print("You`re an adult" if Age>=18 else "You`re a child")