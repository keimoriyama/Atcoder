from bisect import bisect_left, bisect_right
N = int(input())
X = list(map(int,input().split()))
P = list(map(int,input().split()))
Q = int(input())

ruiseki = [0, P[0]]
for i in range(1, len(P)):
    ruiseki.append(ruiseki[-1] + P[i])
    
for _ in range(Q):
    l, r = map(int,input().split())
    pr = bisect_right(X, r)
    pl = bisect_left(X, l)
    print(ruiseki[pr] - ruiseki[pl])
