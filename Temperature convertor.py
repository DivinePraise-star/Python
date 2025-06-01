#temperature convertor

Temp=float(input("Enter temperature: "))
unit=input("Enter unit(C/F): ")

if unit=="C":
    Temp=Temp*(9/5)+32
    unit="degrees Fahrenheit"
    
elif unit=="F":
    Temp=(Temp-32)*5/9
    unit="degrees celcius"
    
else:
    print("Invalid units")
    
print(f"The temperature is {round(Temp,1)} {unit}")    