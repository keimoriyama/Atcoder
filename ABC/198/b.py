N = input()
last_index = len(N)
for i in reversed(range(len(N))):
    if N[i] == '0':
        last_index = i
#print(N[:last_index])
ans = True
for i in range(int(len(N[:last_index])/2)):
    #print(i, last_index-i-1)
    last = last_index-i-1
    if N[i] != N[last]:
        ans = False
        break
if ans:
    print("Yes")
else:
    print("No")