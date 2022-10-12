from math import factorial

P = int(input())
answer = 0
for i in range(10, 0, -1):
    while factorial(i) <= P:
        answer += 1
        P -= factorial(i)
print(answer)
