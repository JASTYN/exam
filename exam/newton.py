from math import sqrt

x = float(input("Enter a number to find its square root: "))
n = 100
guess = x/2

for i in range(n):
    guess = (guess + x/guess)/2

print("Our approximation is %0.15f" % guess)
print("Actual square root is %0.15f" % sqrt(x))
