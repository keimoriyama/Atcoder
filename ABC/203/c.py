n,k = map(int, input().split())
A = [0 for _ in range(10**100)]
for i in range(n):
    a,b = map(int, input().split())
    A[a] += b

money = k
i = 0
ans = 0
while(money > 0):
    ans = i
    money -= 1
    if A[i]:
        money += A[i]
    i+= 1

print(ans)
