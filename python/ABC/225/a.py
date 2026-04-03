S = input()

num_s = set((S[0], S[1], S[2]))
if len(num_s) == 1:
    print(1)
elif len(num_s) == 2:
    print(3)
else:
    print(6)
