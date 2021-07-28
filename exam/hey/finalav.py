def getNumberList(filename):

    f = open(filename,'r')
    #opening the file
    line = f.readline()
    #reading the file line by line
    numbers = line.split(',')
    #The split() method splits a string into a list.
    numberList = []
    #An array to store the list
    
    
    for i in numbers:
        numberList.append(int(i))

    return numberList

def getAverage(numbers):

    sum = 0
    #for storage of the sum of the numbers in the file
    counter = 0
    #for cointing numbers present in the file
    for i in numbers:
        sum = sum + i
        counter = counter + 1

    average = sum/counter
# Getting the average
    return average


def main():

    #user input
    filename = input("Enter filename : ")
    #getting numbers from the required file
    numbers = getNumberList(filename)
    #get the average from the numbers list
    average = getAverage(numbers)
    #display the average
    print(average)
      
if __name__ == "__main__":
    main()