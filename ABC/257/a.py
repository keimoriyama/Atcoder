import string
N, X = map(int, input().split())
X -= 1
c_list = []
for c in string.ascii_uppercase:
    for s in list(c) * N:
        c_list.append(s)

print(c_list[X])
