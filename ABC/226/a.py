X = float(input()) * 10
n = X % 10
if n >= 5:
    X += 10
print(int(X // 10))
