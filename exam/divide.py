money = 100
people = int(input("Enter the number of people: "))
if people < 0:
    print("ERROR: You can't have negative people.")
elif people == 0:
    print("No people. Therefore no money given out.")
elif people == 2:
    print("They each get $50.")
else:
    perperson = money/people
    print("Everyone gets", perperson, "dollars.")
