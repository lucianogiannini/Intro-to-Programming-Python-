import random
numberofheartbeats = int(input("Please enter the number of recorded heartbeats:"))
print("Recorded Heartbeats")
heartbeat = [0]*numberofheartbeats
for i in range(0,numberofheartbeats):
    heartbeat[i] = int(random.uniform(40,150))
print(heartbeat)
maxinterval = 0
interval = 0
total = 0
for i in range(0,numberofheartbeats-1):
    interval = abs(heartbeat[i] - heartbeat[i+1])
    total = total + interval
    if(interval > maxinterval):
        maxinterval = interval
print("Largest interval:",maxinterval)
average = round(total/numberofheartbeats-1)
print("Average interval:",average)
