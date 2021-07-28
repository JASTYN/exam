limit = 10
for item in range(1, 6):
    price = float(input("Enter the price: "))
    message = "Good price. Go ahead and buy."
    if price > limit:
        message = "Too expensive. Do not buy."
    print(message)
