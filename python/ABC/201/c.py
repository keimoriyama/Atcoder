S = input()

mem = []
for i in range(10):
    if S[i] == 'o':
        mem.append(1)
    elif S[i] == 'x':
        mem.append(0)
    elif S[i] == '?':
        mem.append(2)

print(mem)
