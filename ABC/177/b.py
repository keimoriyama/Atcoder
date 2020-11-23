S = input()
T = input()
count = len(T)
tmp = 0
j = 0
i = len(S) - len(T)

while(i >= 0):
    #print(S[i:i+len(T)])
    #print(T[0:i+len(T)])
    for k in range(len(T)):
        if S[i+k] == T[k]:
            #print("S:"+S[i+k]+" T:"+T[k])
            j += 1
        else:
            #print("j:"+str(j))
            tmp = len(T) - j
            #print("tmp:"+str(tmp))
            if count > tmp:
                count = tmp
            tmp = len(T)
    if len(T) == j:
        count = 0
    i -= 1
    j = 0

print(count)
