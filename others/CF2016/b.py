N, A, B = map(int, input().split())
S = input()
C = A + B
p = 0
j = 1
ans, tmp = [],[]

#print(S)
for i in S:
    if i == 'a':
        tmp.append(0)
    elif i == 'b':
        tmp.append(j)
        j += 1
    else:
        tmp.append(0)

#print(tmp)

for i in range(len(S)):
    if S[i] == 'a':
        if p < C:
            ans.append(True)
            p += 1
        else:
            ans.append(False)
    elif S[i] == 'b':
        if (p < C) and (tmp[i] <= B):
            ans.append(True)
            p += 1
        else:
            ans.append(False)
    else:
        ans.append(False)

#print(ans)

for i in ans:
    if i:
        print("Yes")
    else:
        print("No")
