N = int(input())
limit = 2 * N + 1
num_set = set([i for i in range(1, limit + 1)])
while True:
    print(num_set.pop(), flush=True)
    a = int(input())
    if a == 0:
        break
    num_set.discard(a)