S = input()

s = [int(x) for x in S]

reverse = True
for i in range(int(len(s)/2)):
    #print(i, len(s) - i-1)
    if S[i] == S[len(s) - i - 1]:
        continue
    else:
        reverse = False
        break

for i in range(len(s)):
    if s[i] == 9:
        s[i] = 6
    elif s[i] == 6:
        s[i] = 9

if not reverse:
    s.reverse()

s = [str(x) for x in s]
print("".join(s))
