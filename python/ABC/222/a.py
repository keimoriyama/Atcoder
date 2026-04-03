N = input()
if len(N) == 1:
    N = "000" + N
elif len(N) == 2:
    N = "00" + N
elif len(N) == 3:
    N = "0" + N

print(N)
