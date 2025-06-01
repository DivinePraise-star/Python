#calculate the hypotenues of a right angled triangle
import math
a=float(input("Enter the adjacent value, a: "))
b=float(input("Enter opposite value, b: "))

c=math.sqrt(pow(a, 2)+pow(b, 2))

print(f"The hypotenues, c is {round(c, 2)} units.")