M, N = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)

p_dict = {}

for a in A:
    if a not in p_dict.keys():
        p_dict[a] = 1
    else:
        p_dict[a] += 1

s = True

for b in B:
    if b in p_dict.keys():
        if p_dict[b] <= 0:
            s = False
            break
        p_dict[b] -= 1
    else:
        s = False
        break

if s:
    print("Yes")
else:
    print("No")
