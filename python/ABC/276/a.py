S = input()

for i in range(len(S), 0, -1):
    if S[i - 1] == "a":
        print(i)
        exit()

print(-1)
