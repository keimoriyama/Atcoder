S = input()
T = input()

t = 0
for s in S:
    if s == T[t]:
        t += 1
        if t == len(T):
            print("Yes")
            exit()
    else:
        t = 0

print("No")
