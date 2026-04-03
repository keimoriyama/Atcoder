N, M = map(int,input().split())
taro = [False] * (N+1)
for _ in range(M):
    a,b = input().split()
    a = int(a)
    if b == 'M' and not taro[a]:
        print("Yes")
        taro[a]= True
    else:
        print("No")
