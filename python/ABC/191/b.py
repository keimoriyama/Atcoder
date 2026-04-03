N, X = map(int, input().split(' '))
ans = []
tmp = input().split(' ')
# print(tmp)
A = [int(i) for i in tmp]

for a_i in A:
    if a_i != X:
        ans.append(a_i)

if ans:
    for i in ans:
        print(i, end=" ")
else:
    print()