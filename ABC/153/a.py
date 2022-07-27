H, A = map(int, input().split())

n, amari = H // A, H % A

if amari == 0:
    print(n)
else:
    print(n+1)
