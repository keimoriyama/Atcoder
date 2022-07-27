N = int(input())
A = list(map(int, input().split()))

num_dict = {}
for a in A:
    search_list = [a-1, a, a+1]
    for s in search_list:
        if s not in num_dict.keys():
            num_dict[s] = 1
        else:
            num_dict[s] += 1

print(max(num_dict.values()))
