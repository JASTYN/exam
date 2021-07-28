total = 0
count = 0
data = input("Enter a score or just return to quit: ")
while data != "":
    total += int(data)
    count += 1
    data = input("Enter a score or just return to quit: ")
    if count == 0:
        print("No scores were entered.")
    else:
        print("The average is", total / count)