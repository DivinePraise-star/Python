import math

#This is my first python program
print("Hello World!")
print("I miss pizza!")
print("It`s really good!")

firstName="Musiimenta"
print(firstName)
#f-string is used to format and concatnate words
print(f"Hello {firstName}")

food="rice"
print(f"I like {food}")

email="divinepraise699@gmail.com"
print(f"This is my email, {email}")

age=22
print(f"I am aged {age}")

is_student=True
is_retaking=False

if is_student and is_retaking:
    print("I am a retaking student")
    
else:
    print("I am a student")
    
    x=5.5
    y=2.5
    print(x+y)
    
    #types of variables
    print(type(age))
    print(type(firstName))
    print(type(x))
    print(type(is_student))
    
   #typecasting variables str(), float(), bool(), int()
age=float(age)
print(age)
    
is_student= int(is_student)
print(is_student)

age+=1
print(age)

firstName=bool(firstName)
print(firstName)

#input(), allows the user to input data and returns entered data as a string
name=input("What is your name?: ")
age=int(input("How old are you?: "))
age+=1
print(f"My name is {name}, i am {age} years old")


x=3.135
y=-4
z=2
result= round(x)+abs(y)+pow(z, 2)
print(result, max(x,y,z), min(x,y,z))

#built in fuctions in the math class(import math)
print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(2.56))
print(math.floor(2.56))