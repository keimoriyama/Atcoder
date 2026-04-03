A, B = map(int, input().split())

ans = 0
while A != B:
    if A < B:
        if B % A == 0:
            quo = B // A
            B -= (quo - 1) * A
            ans += quo - 1
        else:
            quo = B // A
            B -= A * quo
            ans += quo
    else:
        if A % B == 0:
            quo = A // B
            A -= B * (quo - 1)
            ans += quo - 1
        else:
            quo = A // B
            A -= B * quo
            ans += quo
    if A == 1:
        ans += B - A
        break
    if B == 1:
        ans += A - B
        break

print(ans)
