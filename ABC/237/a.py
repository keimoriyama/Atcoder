N = int(input())
x = 1 << 31
if -x <= N and N < x:
    print("Yes")
else:
    print("No")