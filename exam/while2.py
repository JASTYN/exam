"""
Program to demonstrate
while loop with unknown
number of iterations
"""
totalsales = 0
sales = float(input("Enter a recept item or -1 to stop: "))
while sales != -1:
    totalsales = totalsales + sales
    sales = float(input("Enter a recept item or -1 to stop: "))

print("Total sales for today:", totalsales)
    
