for i in range(5):
    principal = float(input("How much do you want to invest? "))
    rate = 6

    if rate < 0 or rate > 100:
        print("Error: rate must be between 0 and 100.")
    else:
        print("Your will gain", round(rate/100 * principal, 2))
    
