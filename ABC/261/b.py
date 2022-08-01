N = int(input())
A = []
for _ in range(N):
    A.append(input())

ans = True
for i in range(N):
    for j in range(i, N):
        a_i = A[i][j]
        a_j = A[j][i]
        if a_i == "W":
            if a_j != "L":
               ans = False 
        elif a_i == "L":
            if a_j != "W":
                ans = False
        elif a_i == "D":
            if a_j != "D":
                ans = False

if ans:
    print("correct")
else:
    print("incorrect")
