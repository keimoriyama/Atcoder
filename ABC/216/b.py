N = int(input())
Name = []
for _ in range(N):
    s, t = input().split()
    Name.append([s, t])

for i in range(N):
    for j in range(i + 1, N):
        n1 = Name[i]
        n2 = Name[j]
        if n1[0] == n2[0] and n1[1] == n2[1]:
            print("Yes")
            exit()

print("No")
