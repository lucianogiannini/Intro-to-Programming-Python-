ducks = ["Pack", "Nack", "Lack", "Quack", "Kack", "Ouack", "Jack", "Mack"]
print(ducks)
ducks = sorted(ducks)
print(ducks)
ducks.append("Zach")
print(ducks)
corner = ducks.pop(5)
print(ducks)
ducks.insert(2,"Tack")
print(ducks)
ducks = sorted(ducks)
ducks.reverse()
print(ducks)
ducks.insert(2,corner)
print(ducks)
ducks.append("Back")
print(ducks)
leaver = ducks.remove("Zach")
print(ducks)
timeOut = ducks.pop()
print(ducks)
leaver2 = ducks.remove("Tack")
print(ducks)
ducks.append(timeOut)
print(ducks)
leaver3 = ducks.remove("Back")
print(ducks)
print(len(ducks))
print(ducks)
ducks = sorted(ducks)
print(ducks)
