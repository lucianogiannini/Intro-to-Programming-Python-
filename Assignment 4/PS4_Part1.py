import random

numcustomersperhour = int(input("Please enter the average number of customers expeected per hour: "))
numhours = int(input("Please enter the number of hours: "))
customers = numcustomersperhour*numhours
donations = [0.0]*4
counter = 0;
total = 0.0;
for i in range(0,customers):
    if(counter != 3):
        print("Potential Donation")
        donations[counter] = float(format(random.uniform(0.01,0.99),"1.2f"))
        print(donations[counter])
        counter += 1
    
    else:
        print("Potential Donation")
        donations[counter] = format(random.random(),"1.2f")
        print(donations[counter])
        counter = 0;
        index = random.randrange(0,len(donations))
        print("*****Donation made:",donations[index])
        total = total + float(donations[index])
        donations = [0.0]*4
print("Total Donations:")
print('${:,.2f}'.format(total))
