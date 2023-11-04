b = int(input())

for i in range(1, 100):
    if pow(i, i) == b:
        print(i)
        exit()

print(-1)
