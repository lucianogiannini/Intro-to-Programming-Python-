ec = {'Alabama': [9,'U'],'Kentucky' : [8,'U'],'North Dakota' : [3,'U'],'Alaska' : [3,'U'],'Louisiana' : [8,'U'],'Ohio' : [18,'U'],'Arizona' : [11,'U'],
      'Maine' : [4,'U'],'Oklahoma' : [7,'U'],'Arkansas' : [6,'U'],'Maryland' : [10,'U'],'Oregon' : [7,'U'],'California' : [55,'U'],
      'Massachusetts' : [11,'U'],'Pennsylvania' : [20,'U'],'Colorado': [9,'U'],'Michigan' : [16,'U'],'Rhode Island' : [4,'U'],'Connecticut' : [7,'U'],
      'Minnesota' : [10,'U'],'South Carolina' : [9,'U'],'Delaware' : [3,'U'],'Mississippi' : [6,'U'],'South Dakota' : [3,'U'],
      'District of Columbia' : [3,'U'],'Missouri' : [10,'U'],'Tennessee' : [11,'U'],'Florida' : [29,'U'],'Montana' : [3,'U'],
      'Texas' : [38,'U'],'Georgia' : [16,'U'],'Nebraska' : [5,'U'],'Utah' : [6,'U'],'Hawaii' : [4,'U'],'Nevada' : [6,'U'],
      'Vermont' : [3,'U'],'Idaho' : [4,'U'],'New Hampshire' : [4,'U'],'Virginia' : [13,'U'],'Illinois' : [20,'U'],'New Jersey' : [14,'U'],
      'Washington' : [12,'U'],'Indiana' : [11,'U'],'New Mexico' : [5,'U'],'West Virginia' : [5,'U'],'Iowa' : [6,'U'],
      'New York' : [29,'U'],'Wisconsin' : [10,'U'],'Kansas' : [6,'U'],'North Carolina' : [15,'U'],'Wyoming' : [3,'U'], }
for state,vote in ec.items():
    print("Please enter B for Biden or T for Trump")
    canidate = input("Who do you predict will win the state of " + state + ":")
    vote[1] = canidate

bidenvotes = 0
trumpvotes = 0
undecided = 0
for vote in ec.values():
    if vote[1] == 'T':
        trumpvotes = trumpvotes + vote[0]
    elif vote[1] == 'B':
        bidenvotes = bidenvotes + vote[0]
    else:
        undecided = undecided + vote[0]
print("Trump:",trumpvotes)
print("Biden:",bidenvotes)
print("Undecided:",undecided)

if trumpvotes > bidenvotes:
    print("Winner: TRUMP")
elif bidenvotes > trumpvotes:
    print("Winner: BIDEN")
elif trumpvotes == bidenvotes:
    print("TIE")
    
print()
print()

print("States won by Biden")
for state,vote in ec.items():
    if vote[1] == "B":
        print(state)
print()
print()

print("States won by Trump")
for state,vote in ec.items():
    if vote[1] == "T":
        print(state)

print()
print()

print("Undecided States")
for state,vote in ec.items():
    if vote[1] == "U":
        print(state)
