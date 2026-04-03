import string

S = input()
l = list(string.ascii_uppercase)

for i in range(len(S)):
    if S[i] in l:
        print(i + 1)
        exit()
