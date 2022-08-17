A, B = input().split()

for i in range(min(len(A), len(B))):
    if int(A[-i-1]) + int(B[-i-1]) >= 10:
        print("Hard")
        exit()
print("Easy")
