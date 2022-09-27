import string

string_dict = {i: v for i, v in enumerate(string.ascii_lowercase)}
P = list(map(int, input().split()))

ans = ""
for p in P:
    ans += string_dict[p - 1]

print(ans)
