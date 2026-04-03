from collections import Counter


def prime(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f**2 <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


K = int(input())

l = Counter(prime(K))
n_list = []
# pは素数、fはその数が出てくる頻度
for p, f in l.items():
    num = p
    cnt = 1
    # その素数が１より多く含まれる場合
    while cnt < f:
        # 素数をn倍する
        num += p
        n = num
        i = 0
        # nがその素数で何回割れるかを計算する
        while n % p == 0:
            n //= p
            i += 1
        # 割った回数を更新する
        cnt += i
    n_list.append(num)

print(max(n_list))
