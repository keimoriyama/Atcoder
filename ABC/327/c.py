A = [list(map(int, input().split())) for i in range(9)]
for i in range(9):
    ai = set()
    for j in range(9):
        if A[i][j] in ai:
            print("No")
            exit()
        ai.add(A[i][j])

for j in range(9):
    ai = set()
    for i in range(9):
        if A[i][j] in ai:
            print("No")
            exit()
        ai.add(A[i][j])

for i in range(3):
    for j in range(3):
        ai = set()
        for k in range(3):
            for l in range(3):
                if A[3 * i + k][3 * j + l] in ai:
                    print("No")
                    exit()
                ai.add(A[3 * i + k][3 * j + l])

print("Yes")
