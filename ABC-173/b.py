M = int(input())
#リストAにappend()を使って格納していく
a = [input() for i in range(M)]

AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(M):
    if(a[i] == 'AC'):
        AC+=1
    elif(a[i] == 'WA'):
        WA+=1
    elif(a[i] == 'TLE'):
        TLE+=1
    elif(a[i] == 'RE'):
        RE+=1

print("AC x " + str(AC))
print("WA x " + str(WA))
print("TLE x " + str(TLE))
print("RE x " + str(RE))
