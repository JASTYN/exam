from functools import reduce

file = open("PY.txt","r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1   
print(Counter)

def average(num):
    sum_num = 0
    for x in num:
        sum_num = sum_num + x           
    avg = sum_num / len(num)

    return avg



print("The average is", average(Colist))