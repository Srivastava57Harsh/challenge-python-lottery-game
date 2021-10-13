import random
local=[]
for i in range(6):
    n=random.randint(1,100)
    while n in local:
        n=random.randint(1,100)
    local.append(n)
print("ENTER YOUR 6 TICKET NUMBERS:-  ")
temp=[]
for i in range (6):
    ticket=int(input())
    if ticket in local:
        temp.append(ticket)
if len(temp)==0:
    print("NO TICKETS MATCHED")
else:
    for i in temp:
        print("Great, Your ",len(temp)-1," matched") 
