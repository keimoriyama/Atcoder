N = int(input())
S = input()

ans = 0
for i in range(N-2):
    if S[i] == "#" and S[i+2] == "#" and S[i+1] == ".":
        ans += 1

print(ans)
