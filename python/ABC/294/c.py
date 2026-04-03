N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

i, j,idx = 0, 0, 1
ai, bj = [], []
while True:
    if A[i]<B[j]:
        ai.append(idx)
        i += 1
    else:
        bj.append(idx)
        j += 1
    if len(A) <= i or len(B) <= j:
        break
    idx += 1

if len(ai) != len(A):
    while len(A) > len(ai):
        idx+=1
        ai.append(idx)
if len(bj) != len(B):
    while len(B) > len(bj):
        idx+=1
        bj.append(idx)

print(*ai)
print(*bj)

