import math

status = 'Odd'
number = int(input("Enter a number: "))
x = number % 2
if x == 0:
    status = 'Even'
    
print("Your number is", status)

if number < 0:
    print("A circle can't have a negative radius.")
else:
    area = math.pi * number * number
    print("The area of the circle is ", area) 
