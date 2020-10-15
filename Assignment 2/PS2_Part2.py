number_of_cookies = int(input("Please enter the number of cookies you want to bake: "))
cup_of_sugar_one_cookie = 1.5/48
cup_of_butter_one_cookie = 1.0/48
cup_of_flour_one_cookie = 2.75/48

#print(cup_of_sugar_one_cookie,cup_of_butter_one_cookie,cup_of_flour_one_cookie)

cups_of_sugar = number_of_cookies*cup_of_sugar_one_cookie
cups_of_butter = number_of_cookies*cup_of_butter_one_cookie
cups_of_flour = number_of_cookies*cup_of_flour_one_cookie


print("You will need:")
print(format(cups_of_sugar, "<2.3f")," cups of sugar")
print(format(cups_of_butter, "<2.3f")," cups of butter")
print(format(cups_of_flour, "<2.3f")," cups of flour")
