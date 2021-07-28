from math import sqrt

x = float(input("Enter a number to find its square root: "))

count = 0
guess = x/2
tolerance = 0.00001
while (guess * guess - x) > tolerance:
    guess = (guess + x/guess)/2
    count += 1

# print("Our approximation is %0.15f" % guess)
# print("Actual square root is %0.15f" % sqrt(x))
print(f'Our approximation is{guess: .15f}')
print(f'Actual squre root is{sqrt(x): .15f}')
print("The number of iterations was", count)
