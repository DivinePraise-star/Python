#weight convertor

weight=float(input("Enter weight: "))
unit=input("Kilograms or pounds? (Kgs, Lbs): ")

if unit=="Kgs":
    weight=weight*2.205
    unit="Lbs"
    print(f"Your weight is {round(weight,2)}{unit}")
elif unit=="Lbs":
    weight/=2.205
    unit="Kgs"
    print(f"Your weight is {round(weight,2)}{unit}")
else:
    print(f"Invalid units")
    

    