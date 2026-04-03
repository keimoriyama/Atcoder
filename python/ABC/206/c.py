N = input()
A = map(int, input().split())

A = list(set(A))

# print(A)
print(int(len(A) * (len(A) - 1) / 2))
