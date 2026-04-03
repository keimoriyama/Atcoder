Q = int(input())

num, count = [], []
for _ in range(Q):
    query = list(map(int, input().split()))
    # print(f"query: {query}")
    if query[0] == 1:
        x, c = query[1], query[2]
        num.append(x)
        count.append(c)
    elif query[0] == 2:
        ans = 0
        c = query[1]
        """
        if count[0] > c:
            ans = c * num[0]
            count[0] -= c
        """
        while c > 0:
            # print(f"c: {c} num: {num} count: {count}")
            if count[0] >= c:
                ans += c * num[0]
                count[0] -= c
                c = 0
            else:
                ans += count[0] * num[0]
                c -= count[0]
                count.pop(0)
                num.pop(0)
        print(ans)
    # print(f"num: {num} count: {count}")