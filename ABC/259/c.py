def make_list(s):
    num = 1
    s_list = []
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            s_list.append([s[i-1], num])
            num = 1
        else:
            num += 1
    s_list.append([s[-1], num])
    return s_list


s = input()
t = input()
num = 1
s_list, t_list = make_list(s), make_list(t)
ans = True
for s, t in zip(s_list, t_list):
    if s[0] != t[0]:
        ans = False
    elif s[1] < t[1] and s[1] == 1:
        ans = False
    elif t[1] < s[1]:
        ans = False
if len(s_list) != len(t_list):
    ans = False
if ans:
    print("Yes")
else:
    print("No")