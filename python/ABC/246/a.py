x, y = [], []
for _ in range(3):
    x1, y1 = input().split()
    x.append(x1)
    y.append(y1)

ans_x, ans_y = 0, 0
if x[0] == x[1]:
    ans_x = x[2]
elif x[1] == x[2]:
    ans_x = x[0]
else:
    ans_x = x[1]
if y[0] == y[1]:
    ans_y = y[2]
elif y[2] == y[0]:
    ans_y = y[1]
else:
    ans_y = y[0]
print(ans_x, ans_y)