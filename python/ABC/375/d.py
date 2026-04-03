from string import ascii_uppercase
S = input()

ans = 0
cnt, sum = [0]* 26, [0]*26
char2idx = {c: i for i, c in enumerate(ascii_uppercase)}

for i, si in enumerate(S):
    idx = char2idx[si]
    ans += (i-1)*cnt[idx] - sum[idx]
    cnt[idx] += 1
    sum[idx] += i

print(ans)
