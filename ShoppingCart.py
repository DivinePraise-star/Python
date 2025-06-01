#shopping cart program
item=input("Enter item you want to purchase: ")
price=float(input("Enter item price: "))
quantity=int(input("Enter quantity purchased: "))
total=price*quantity

print(f"Item name: {item}     Item price: ${price}     Quantity pruchased: {quantity}      Total paid: ${total}.")