a, b = map(int, input().split())


def judge(n):
    list = set()
    if n == 1:
        list = [1]
    elif n == 2:
        list = [2]
    elif n == 3:
        list = [1, 2]
    elif n == 4:
        list = [4]
    elif n == 5:
        list = [1, 4]
    elif n == 6:
        list = [2, 4]
    elif n == 0:
        list = [0]
    else:
        list = [1, 2, 4]
    return set(list)


a = judge(a) | judge(b)
print(sum(list(a)))
