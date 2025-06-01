response = input("Would you like to register with us?(Y/N): ")

if response=="Y":
        Full_Name=str(input("Enter your full name: "))
        Age=int(input("Enter your age: "))
        Date_Of_Birth=input("Enter your date of birth: ")
        Country=input("Enter your country: ")
        print(f"{Full_Name}, you are now registered.")
        
else:
    print("Thank you for your response. Enjoy!!")