L, R = map(int, input().split())


def count_num(n):
    digit, cnt = 1, 0
    while True:
        u = 10 ** (digit-1)-1
        t = min(n, 10 ** digit - 1)
        cnt += ((t * (t + 1) - u * (u+1))//2) * digit
        if n <= 10 ** digit - 1:
            return cnt
        digit += 1


print((count_num(R) - count_num(L - 1)) % (10 ** 9 + 7))
