N = input()

if N[len(N) - 1] == "s":
    N += "es"
else:
    N += "s"
print(N)
