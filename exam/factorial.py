"""
a factorial of n is 1 X 1 X 3 X ... X n
"""
n = int(input("Enter a number: "))

product = 1

for count in range(1, n + 1):
    product = product * count

print(f'The factorial of {n} is {product}')
