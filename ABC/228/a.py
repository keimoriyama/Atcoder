S, T, X = map(int, input().split())
if S > T:
    if S <= X or X < T:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
if S <= X and X < T:
    print("Yes")
    exit()
else:
    print("No")
    exit()
