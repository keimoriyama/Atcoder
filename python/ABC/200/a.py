N = int(input())

if N % 100 == 0:
    c = int(N/100)
else:
    c = int(N/100) + 1

print(c)
