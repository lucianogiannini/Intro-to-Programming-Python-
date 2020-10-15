dog_years = int(input("Please enter the number of completed years: "))
dog_months = int(input("Please enter the number of completed months:"))
if dog_years > 1 :
    human_years = (dog_years-1) * 6.0 + 7
    #print(human_years)
    human_months = ((dog_months/12) * 6)
    #print(human_months)
    age = human_years + human_months
    print("Your dog is:", age, "years old")
else :
    print((dog_months/12) * 7)
    
