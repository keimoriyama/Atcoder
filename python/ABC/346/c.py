N, K = map(int, input().split())
A = list(set(list(map(int, input().split()))))

A = [a for a in A if a <= K]

sum_all = K * (1 + K)
sum_all -= 2 * sum(A)

print(sum_all // 2)
