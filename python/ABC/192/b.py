from string import ascii_lowercase, ascii_uppercase

lower = list(ascii_lowercase)
upper = list(ascii_uppercase)

S = input()
for i, s in enumerate(S):
    i += 1
    if i % 2 == 0 and s not in upper:
        print("No")
        exit()
    if i % 2 == 1 and s not in lower:
        print("No")
        exit()

print("Yes")
