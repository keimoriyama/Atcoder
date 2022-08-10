import string

alphabet = list(string.ascii_lowercase)
d, d_1 = {}, {}
for i, a in enumerate(alphabet):
    d[a] = i
    d_1[i] = a


S = input()
T = input()

for k in range(26):
    c = "".join([d_1[(d[n_t] + k) % 26] for n_t in T])
    if c == S:
        print("Yes")
        exit()
print("No")
