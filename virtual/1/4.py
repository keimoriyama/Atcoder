N = int(input())

paper = set()
for _ in range(N):
    A = int(input())
    if A in paper:
        paper.discard(A)
    else:
        paper.add(A)

print(len(paper))
