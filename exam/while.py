"""
Program to add the numbers
1 to 10
"""
sum = 0
for i in range(1, 11):
    sum = sum + i
    print(i, sum)


print("Now using while...")

n = 1
total = 0

while n <= 10:
    total = total + n
    print(n, total)
    n = n + 1
