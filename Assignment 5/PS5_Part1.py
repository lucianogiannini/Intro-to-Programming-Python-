import random
numbers = [];
daily = [];
size = 365;
for i in range(365):
    for j in range(4):
        daily.append(random.randint(0,9))
    numbers.append(daily)
    daily = []
#print(numbers)
totalsum = 0
avgtotal = 0
for i in numbers:
    totalsum = totalsum + i[0]
    #print(i[0])
    totalsum = totalsum + i[1]
    #print(i[1])
    totalsum = totalsum + i[2]
    #print(i[2])
    totalsum = totalsum + i[3]
    #print(i[3])
avgtotal = int(totalsum/365)
print("The average of the total of the 4 digits drawn each day is:",avgtotal)

firstevenandlastodd = 0

for i in numbers:
    if i[0] == 2 or i[0] == 4 or i[0] == 6 or i[0] == 8 or i[0] == 0:
        if i[3] == 1 or i[3] == 3 or i[3] == 5 or i[3] == 7 or i[3] == 9:
            firstevenandlastodd = firstevenandlastodd + 1
percent = (firstevenandlastodd/size) * 100
print("Percent of the first digit of the 4 digits drawn is even and the last digit is odd is:",format(percent, "2.2f"),"%")

middletwosame = 0;
everythingelse = 0;

for i in numbers:
    if i[1] == i[2]:
        middletwosame = middletwosame + 1
percentofmiddletwosame = (middletwosame/size) * 100
print("Percent that the middle digits of the 4 digits drawn are the same:",format(percentofmiddletwosame,"2.2f"),"%")

count_of_numbers = [0,0,0,0,0,0,0,0,0,0]
for i in range(13*7):
    first = numbers[i][0]
    second = numbers[i][1]
    third = numbers[i][2]
    fourth = numbers[i][3]
    
    count_of_numbers[first] = count_of_numbers[first] + 1
    count_of_numbers[second] = count_of_numbers[second] + 1
    count_of_numbers[third] = count_of_numbers[third] + 1
    count_of_numbers[fourth] = count_of_numbers[fourth] + 1
indexofhighestnumberfreq = count_of_numbers.index(max(count_of_numbers))
print("Digit",indexofhighestnumberfreq,"has the highest frequency in the first quarter")

numberofeven = 0
numberofodd = 0;
for i in numbers:
    if i[0] == 2 or i[0] == 4 or i[0] == 6 or i[0] == 8 or i[0] == 0:
        numberofeven = numberofeven + 1
    if i[1] == 2 or i[1] == 4 or i[1] == 6 or i[1] == 8 or i[1] == 0:
        numberofeven = numberofeven + 1
    if i[2] == 2 or i[2] == 4 or i[2] == 6 or i[2] == 8 or i[2] == 0:
        numberofeven = numberofeven + 1
    if i[3] == 2 or i[3] == 4 or i[3] == 6 or i[3] == 8 or i[3] == 0:
        numberofeven = numberofeven + 1
    if i[0] == 1 or i[0] == 3 or i[0] == 5 or i[0] == 7 or i[0] == 9:
        numberofodd = numberofodd + 1
    if i[1] == 1 or i[1] == 3 or i[1] == 5 or i[1] == 7 or i[1] == 9:
        numberofodd = numberofodd + 1
    if i[2] == 1 or i[2] == 3 or i[2] == 5 or i[2] == 7 or i[2] == 9:
        numberofodd = numberofodd + 1
    if i[3] == 1 or i[3] == 3 or i[3] == 5 or i[3] == 7 or i[3] == 9:
        numberofodd = numberofodd + 1
if numberofeven > numberofodd:
    print("Even numbers are more common")
elif numberofeven < numberofodd:
    print("Odd numbers are more common")
elif numberofeven == numberofodd:
    print("There are equal number of even and odd numbers")

allsame = 0;
for i in numbers:
    if i[0] == i[1] and i[1] == i[2] and i[2] == i[3]:
        allsame = allsame + 1
print("There were",allsame,"calls that had all the same number")
