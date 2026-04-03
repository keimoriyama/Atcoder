def f(x):
    return x * (x + 1) // 2


from math import gcd, floor

N, A, B = map(int, input().split())

C = (A * B) // gcd(A, B)
m = N // A
k = N // B
l = N // C

ans = 0
ans += f(N)
# print(ans)
ans -= A * f(N // A)
# print(A * f(N // A))
ans -= B * f(N // B)
# print(B * f(N // B))
ans += C * f(N // C)
# print(C * f(N // C))
print(int(ans))
