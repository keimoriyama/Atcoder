N = int(input())
A = sorted(list(map(int, input().split())))

A_odd = [a for a in A if a % 2 != 0]
A_even = [a for a in A if a % 2 == 0]

max_odd, max_even = 0, 0
if len(A_odd) >= 2:
    max_odd = A_odd[-1] + A_odd[-2]

if len(A_even) >= 2:
    max_even = A_even[-1] + A_even[-2]

if max_odd == 0 and max_even == 0:
    print(-1)
else:
    print(max(max_even, max_odd))
