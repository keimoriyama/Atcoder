N = int(input())
S = input()

i = 0
for s in S:
    if s == "1":
        break
    i += 1

if i % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
