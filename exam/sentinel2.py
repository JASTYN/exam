rec = input("Enter a receipt: ")
total = 0
count = 0

while True:
    if rec == "":
        break
    receipt = float(rec)
    total += receipt
    count += 1
    rec = input("Enter a receipt: ")

print(f'Today you made {total: .2f}') # formatting using the f-string instead of %
print(f'You sold {count} items')

