X = int(input())
ans = X - (X // 100) * 100
if ans == 0:
    print(100)
else:
    print(100 - ans)
