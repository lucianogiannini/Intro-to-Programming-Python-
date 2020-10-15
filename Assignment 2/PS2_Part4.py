population = int(input("Please enter the total population"))
pop_uninfected = population
first_month = pop_uninfected * .5
pop_uninfected = pop_uninfected - first_month
second_month = pop_uninfected * .4
pop_uninfected = pop_uninfected - second_month
third_month = pop_uninfected * .3
pop_uninfected = pop_uninfected - third_month
fourth_month = pop_uninfected * .2
pop_uninfected = pop_uninfected - fourth_month
fifth_month = pop_uninfected * .1
pop_uninfected = pop_uninfected - fifth_month
print("Number of people infected in the first Month:", int(first_month))
print("Number of people infected in the second Month:", int(second_month))
print("Number of people infected in the third Month:", int(third_month))
print("Number of people infected in the fourth Month:", int(fourth_month))
print("Number of people infected in the fifth Month:", int(fifth_month))

popinfected = first_month + second_month + third_month + fourth_month + fifth_month
print("Total number of people infected:", int(popinfected))

print("Total number of people not infected:", int(pop_uninfected))
