from collections import defaultdict

S = input()

d = defaultdict(list)

for i, s in enumerate(S):
    d[s].append(i + 1)


b_pos = d["B"]
check_b = ((b_pos[0] % 2 == 1) and (b_pos[1] % 2 == 0)) or (
    (b_pos[0] % 2 == 0) and (b_pos[1] % 2 == 1)
)

r_pos = d["R"]
k_pos = d["K"]
check_pos = r_pos[0] < k_pos[0] < r_pos[1]
if check_b and check_pos:
    print("Yes")
else:
    print("No")
