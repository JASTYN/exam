mark = int(input("Enter a numeric mark: "))

while mark < 0 or mark > 100:
    mark = int(input("Error. Invalid input. Try again: "))

if mark >= 90:
    grade = 'A'
elif mark >= 80:
    grade = 'B'
elif mark >= 70:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)
