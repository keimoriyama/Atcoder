N = int(input())
dict = {}
for _ in range(N):
    S = input()
    if S not in dict.keys():
        print(S)
        dict[S] = 1
    else:
        print(S + "(" + str(dict[S]) + ")")
        dict[S] += 1
