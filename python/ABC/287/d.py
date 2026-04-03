S = input()
T = input()
N = len(T)


def check(a, b):
    return a == "?" or b == "?" or a == b


pre = [False] * len(S)
suf = [False] * len(S)
pre[0] = True
for i in range(len(T)):
    if not check(S[i], T[i]):
        break
    pre[i + 1] = True

S = list(reversed(S))
T = list(reversed(T))
for i in range(len(T)):
    if not check(S[i], T[i]):
        break
    suf[i + 1] = True
suf[0] = True

for i in range(len(T) + 1):
    if pre[i] and suf[len(T) - i]:
        print("Yes")
    else:
        print("No")
