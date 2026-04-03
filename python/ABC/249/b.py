S = input()
list, u_l = [], []
good, upper, lower = True, False, False
for s in S:
    if s not in list:
        list.append(s)
    else:
        good = False
    if s.isupper():
        upper = True
    if s.islower():
        lower = True
if good and upper and lower:
    print("Yes")
else:
    print("No")