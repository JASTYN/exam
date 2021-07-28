mark = int(input("Enter a numeric mark or 999 to stop: "))

while mark != 999:
    if mark >= 0 and mark <= 100:
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
    else:
        print("Invalid mark")
    mark = int(input("Enter another mark or 999 to stop: "))
        
