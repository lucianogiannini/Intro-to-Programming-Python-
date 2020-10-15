import random
myList = []
sales = []
for i in range(52):
    for j in range(7):
        sales.append(random.randint(70,100))
    myList.append(sales)
    sales = []
print(myList)
highestsaleoftheweek = [0]*7
for i in myList:
    index = i.index(max(i))
    highestsaleoftheweek[index] = highestsaleoftheweek[index] + 1
print()
print(highestsaleoftheweek)
