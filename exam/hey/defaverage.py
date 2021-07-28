from statistics import mean

def Average(lst):
   return mean(lst)

# Driver Code
lst = open('PY.txt')
average = Average(lst)

# Printing average of the list
print("Average of the list =", average)