from random import randint
myList = [1, 2, 3, 4, 5, 6, 7]
length_of_myList = len(myList)
inc = 0
printed_values = []
while len(printed_values) != length_of_myList:
    value = randint(0,len(myList)-1)
    #print(i,value)
    print(myList[value])
    printed_values.append(myList[value])
    myList.remove(myList[value])
