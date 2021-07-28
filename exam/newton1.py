from math import sqrt

x = float(input("Enter a number to find its square root: "))
n = 10
guess = x/2

count = 1
while count <= n:
    guess = (guess + x/guess)/2
    print(guess)
    count = count + 1 # count += 1 not count++

print("Our approximation is %0.15f" % guess)
print("Actual square root is %0.15f" % sqrt(x))
