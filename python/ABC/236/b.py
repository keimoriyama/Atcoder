N = int(input())
A = list(map(int, input().split()))
num_list = {}

for a in A:
    if a not in num_list.keys():
        num_list[a] = 1
    else:
        num_list[a] += 1

for k, v in zip(num_list.keys(), num_list.values()):
    if v != 4:
        print(k)
