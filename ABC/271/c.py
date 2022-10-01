N = int(input())
A = list(map(int, input().split()))
books = [False] * (N + 2)
sold = 0
for a in A:
    if a >= len(books):
        sold += 1
    elif books[a]:
        sold += 1
    else:
        books[a] = True

L, R = 1, N + 1

while True:
    while books[L]:
        L += 1
    while R != 0 and not books[R]:
        R -= 1
    if sold >= 2:
        sold -= 2
        books[L] = True
    else:
        if L >= R:
            break
        books[R] = False
        sold += 1


print(L - 1)
