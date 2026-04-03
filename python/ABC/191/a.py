V, T, S, D = map(int, input().split(' '))

hit_time = D / V

if T <= hit_time and hit_time <= S:
    print('No')
else:
    print('Yes')