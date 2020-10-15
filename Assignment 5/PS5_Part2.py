phonebill = [["Kiera", [11,21,13,14,15,60,38], "508-111-1110"], 
             ["Lorenzo", [20,12,33,26,37,62,70],"508-111-1111"], 
             ["Mabel", [31,27,43,7,52,68,5],"508-111-1112"],
             ["Nikolai", [8,7,212,28,114,30,39],"508-111-1113"]]

for i in phonebill:
    lowestminused = min(i[1])
    highestminused = max(i[1])
    total = sum(i[1])
    counter = len(i[1])
    averageminused = total/counter
    i.append(lowestminused)
    i.append(highestminused)
    i.append(averageminused)
    
print(phonebill)
