from itertools import permutations

S, K = input().split()
S = [s for s in S]

string = set()
for v in permutations(S):
    string.add("".join(list(v)))
print(sorted(list(string))[int(K) - 1])
