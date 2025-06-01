#logical operators

temp=float(input("Enter temperature: "))
condition=input("Enter weather condition(sunny/rainy/cloudy/windy): ")

if 35>temp>25 and condition=="sunny":
    print("The weather is hot!!")
elif 25>temp>20 and condition=="windy":
    print("The weather is warm!!")
elif 20>temp>15 and condition=="cloudy":
    print("It`s going to rain")
elif temp<15 and condition=="rainy":
    print("It`s raining coldness")
    
else:
    print("Burnout temperatures")
    
    